import numpy as np
from math import sqrt
import random as rd
from copy import deepcopy
import os

def distancia_pontos(x1,y1,x2,y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

entrada = open('in.txt','r')
n = int(entrada.readline())
pontos = []
for i in range(0,n):
    idx,x,y = entrada.readline().split()
    pontos.append((int(idx),float(x),float(y)))
entrada.close()
entrada = open('tour.txt','r')
tour = []
for i in range(0,n):
    tour.append(int(entrada.readline())-1)
vet = np.zeros(shape=(n+1,n+1))
for i in range(0,n):
    for j in range(0,n):
        vet[i][j]=distancia_pontos(pontos[i][1],pontos[i][2], pontos[j][1], pontos[j][2])

class genetic_algorithm:
    __ncid = int()
    __tam_populacao = int()
    __taxa_mutacao = int()
    __populacao = []
    __melhor_caminho=[]
    __melhor_distancia=100000000
    def __calucula_adaptabilidade(self, cromossomo):
        valor = 0
        for i in range(0,self.__ncid):
            x = int(cromossomo[i])
            y = int(cromossomo[(i+1)%self.__ncid])
            valor += vet[x][y]
        return valor

    def __gera_populacao(self):
        cromossomo = []
        i=0
        while i < self.__ncid:
            cromossomo.append(i)
            i+=1
        populacao = []
        for i in range(0,self.__tam_populacao):
            rd.shuffle(cromossomo)
            populacao.append(deepcopy(cromossomo))
        self.__populacao =  populacao

    def __gera_filho(self,x,y):
        pos = [0 for i in range(0,self.__ncid)]
        aux = []
        for i in range(0,self.__ncid):
            aux.append((i,x[i]))
        for i in range(0, self.__ncid):
            aux.append((i, y[i]))
        aux.sort()
        filho = []
        for i in aux:
            if pos[i[1]] == 0:
                filho.append(i[1])
                pos[i[1]] = 1
        return filho



    def __cruzamento(self):
        filhos = []
        for i in range(0,int(self.__tam_populacao/2)):
            x = rd.choice(self.__populacao)
            y = rd.choice(self.__populacao)
            while x == y:
                y = rd.choice(self.__populacao)
            filhos.append(self.__gera_filho(x,y))
        return filhos

    def __selecao(self,filhos):
        for i in filhos:
            self.__populacao.append(i)
        elitismo = []
        for i in self.__populacao:
            elitismo.append((self.__calucula_adaptabilidade(i),i))
        elitismo.sort()
        if elitismo[0][0] < self.__melhor_distancia:
            self.__melhor_distancia, self.__melhor_caminho = elitismo[0][0], elitismo[0][1]

        nova_populacao = []
        for i in range(0,self.__tam_populacao):
            nova_populacao.append(elitismo[i][1])
        self.__populacao = nova_populacao

    def __mutacao(self):
       for i in self.__populacao:
            k=rd.randint(0,100)
            if k < self.__taxa_mutacao:
                rd.shuffle(i)



    def __init__(self, n, tam_populacao, taxa_mutacao,comparacao):

        self.__ncid = n
        self.__tam_populacao = tam_populacao
        self.__taxa_mutacao = taxa_mutacao
        self.__gera_populacao()
        anterior = 0
        itr = 0
        h = 1
        while 1==1:
            filhos = self.__cruzamento()
            self.__selecao(filhos)
            #self.__mutacao()
            if anterior == self.__melhor_distancia:
                itr+=1
            else:
                anterior = self.__melhor_distancia
                itr=0
            h+=1
            if itr == 5000:
                self.__gera_populacao()
            print(h,itr,self.__melhor_distancia, comparacao)


def calucula_1():
    valor = 0
    for i in range(0,len(tour)):
        x = int(tour[i])
        y = int(tour[(i+1)%len(tour)])
        valor += vet[x][y]
    return valor

opa = 426.00
ga = genetic_algorithm(n,500,5,opa)










