#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <set>
#include <map>
#include <string>
#include <stack>
#include <bitset>
#include <stdlib.h>
#include <random>
using namespace std;
#define ull unsigned long long int
#define ll long long int
#define pb push_back
#define mp make_pair
#define fast_io cin.tie(0), cin.sync_with_stdio(false);
#define PI 3.14159265359
#define eps 1e-9
#define unvisited -1
typedef vector<int>vi;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef pair<int, string> istr;
typedef vector<istr> vistr;
typedef vector< vector<int> > vvi;
typedef vector< vector<ii> > vvii;
const int ox[8]={1,0,-1,0,1,-1,1,-1};
const int oy[8]={0,1,0,-1,1,-1,-1,1};
const int inf = 1000000001;
const int mod = 1e9+7;
const int tam = 31622777;
const long long int big_lim = 2147483647;
struct ponto
{
	double x,y;
	ponto(double a, double b)
	{
		x=a;
		y=b;
	}
};
double distancia_entre_dois_pontos(ponto a,ponto b)
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
class GA
{
	private:
		vector< vector<int> >populacao;
		vector< double > adaptabilidade; 
		int taxa_mutacao;
		vector<int>pai,mae,f1,f2;
		int melhor;
	public:
		void gera_populacao(int tam_populacao,int numero_de_genes)
		{
			vector<int> cromossomo_auxiliar;
			for(int i=0; i<numero_de_genes; i++)
				cromossomo_auxiliar.pb(i);
			while(tam_populacao--)
			{
				random_shuffle(cromossomo_auxiliar.begin(), cromossomo_auxiliar.end());

				populacao.pb(cromossomo_auxiliar);

			}
		}
		void calculo_adaptabilidade(vector<ponto> &conj)
		{
			for(int i=0;i<populacao.size();i++)
			{
				double valor=0;
				for(int j=1; j<populacao[i].size();j++)
				{
					valor+=distancia_entre_dois_pontos(conj[populacao[i][j]],conj[populacao[i][j-1]]);
				}
				valor+=distancia_entre_dois_pontos(conj[populacao[i][0]],conj[populacao[i][populacao[i].size()-1]]);
				adaptabilidade.pb(valor);
			}
		}
		double calculo_adaptabilidade_individual(vector<ponto> &conj, vi &a)
		{
			double valor = 0;
			for(int j=1; j<a.size();j++)
			{
				valor+=distancia_entre_dois_pontos(conj[a[j]],conj[a[j-1]]);
			}
			valor+=distancia_entre_dois_pontos(conj[a[0]],conj[a[a.size()-1]]);
			return valor;
		}
		void selecao_pais()
		{
			random_device device;
			unsigned int idx = device()%populacao.size();
			int idx1=device()%populacao.size();
			while(idx1 == idx)
			{
				idx1=device()%populacao.size();
			}
			pai = populacao[idx];
			mae = populacao[idx1];
		}
		void corrige_filho(vi &a)
		{
			int tam = a.size();
			int rep[tam];
			memset(rep,0,sizeof(rep));
			vi elementos;
			for(int i=0;i<tam;i++)
				rep[a[i]]++;
			for(int i=0;i<tam;i++)
			{
				if(rep[i] == 0)
					elementos.pb(i);
			}
			int k=0;
			for(int i=0;i<tam;i++)
			{
				if(rep[a[i]] > 1)
				{
					rep[a[i]] --; 
					a[i] = elementos[k];
					rep[a[i]] ++; 
					k++;
				}
			}
		}
		void cruzamento()
		{
			random_device device;
			f1.clear();
			f2.clear();
			for(int i=0;i<pai.size();i++)
			{
				unsigned int r = device()%2;
				if(r)
					f1.pb(pai[i]);
				else
					f1.pb(mae[i]);
			}
			for(int i=0;i<pai.size();i++)
			{
				unsigned int r = device()%2;
				if(r)
					f2.pb(pai[i]);
				else
					f2.pb(mae[i]);
			}
			corrige_filho(f1);
			corrige_filho(f2);
		}
		void mutacao(int taxa, vi &a)
		{
			random_device device;
			unsigned int r = device()%100;
			if(r<taxa)
			{
				int idx = device()%a.size();
				int idx1 = device()%a.size();
				while(idx == idx1)
				{
					idx1 = device()%a.size();
				}
				swap(a[idx],a[idx1]);
			}
		}
		void selecao(vi &a, vector<ponto> &conj)
		{
			int idx = 0;
			for(int i=0;i<populacao.size();i++)
			{
				if(adaptabilidade[idx] < adaptabilidade[i])
					idx = i;
			}
			adaptabilidade[idx] = calculo_adaptabilidade_individual(conj, a);
			populacao[idx] = a;
		}
		void resposta()
		{
			int idx = 0;
			for(int i=0;i<adaptabilidade.size();i++)
			{
				if(adaptabilidade[idx] > adaptabilidade[i])
					idx = i;
			}
			melhor = idx;
		}
		vi caminho()
		{
			return populacao[melhor];
		}
		double tamanho_caminho(vector<ponto> &conj)
		{
			return calculo_adaptabilidade_individual(conj,populacao[melhor]);
		}
		GA(int tam_populacao, vector<ponto> &conj, int taxa_de_mutacao, int numero_de_genes, int numero_de_geracoes)
		{
			gera_populacao(tam_populacao,numero_de_genes);
			calculo_adaptabilidade(conj);
			while(numero_de_geracoes--)
			{
				selecao_pais();
			
				cruzamento();
			
				mutacao(taxa_mutacao, f1);
				mutacao(taxa_mutacao, f2);
		
				selecao(f1,conj);
				selecao(f2,conj);
			}
			resposta();
		}
};

int main()
{
	vector <ponto> conj;
	int n;
	cin>>n;
	double x,y;
	for(int i=0;i<n;i++)
	{
		cin>>x>>y;
		conj.pb(ponto(x,y));
	}
	GA solver(1000, conj, 4, n,10000);
	cout<<solver.tamanho_caminho(conj)<<endl;
	vi ans = solver.caminho();
	for(int i=0;i<ans.size();i++)
	{
		cout<<ans[i]<<" ";
	}
	puts("");
}