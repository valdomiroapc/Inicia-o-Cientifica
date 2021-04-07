class modulo:
    capacity = float()
    cost = float()
    def __init__(self, cap,cost):
        self.capacity = float(cap)
        self.cost = float(cost)

    def print_modulo(self):
        print('capacity:',self.capacity,'cost:',self.cost)

class demanda:
    o = int()
    d = int()
    v = float()
    id = str()
    def __init__(self,origem,destino,volume,nome):
        self.o = origem
        self.d = destino
        self.v = volume
        self.id = nome

class link:
    o = int()
    d = int()
    o_name = str()
    d_name = str()
    name = str()
    pre_installed_capacity = float()
    pre_installed_capacity_cost = float()
    routing_cost = float()
    setup_cost = float()
    def __init__(self,o,d,o_name,d_name,name,pre_installed_capacity,pre_installed_capacity_cost,routing_cost,setup_cost,module_list):
        self.o = int(o)
        self.d = int(d)
        self.o_name = o_name
        self.d_name = d_name
        self.name = name
        self.pre_installed_capacity = float(pre_installed_capacity)
        self.pre_installed_capacity_cost = float(pre_installed_capacity_cost)
        self.routing_cost = float(routing_cost)
        self.setup_cost = float(setup_cost)
        self.module_list = module_list

    def print_link(self):
        print('---dados do link---')
        print('nome:',self.name,'\nnome origem:',self.o_name,'\nnome destino:',self.d_name,'\nnumero origem:',self.o,'\nnumero destino:',self.d,'\npre_installed_capacity:',self.pre_installed_capacity,'\npre_installed_capacity_cost:',self.pre_installed_capacity_cost,'\nrouting cost:',self.routing_cost,'\nsetup_cost:',self.setup_cost)
        print('lista de modulos:',len(self.module_list))
        c=0
        print( type(self.module_list[0]))
        for i in self.module_list:
            self.module_list[c].print_modulo()
            c+=1

class no:
    nome = str()
    coordenada_x = float()
    coordenada_y = float()
    def __init__(self,nome,cx,cy):
        self.coordenada_x = cx
        self.coordenada_y = cy
        self.nome = nome
    def print_no(self):
        print('nome:',self.nome,'coordenada x:',self.coordenada_x,'coordenada y:',self.coordenada_y)

class grafo_teleco:
    __vertices = {}
    __links = {}
    __demands = {}
    nos = []
    E = []
    D = []
    def __le_vertices(self):
        arq = open(r'instancia1/nodes', 'r')
        while True:
            linha=arq.readline().split()
            if len(linha) == 0:
                break
            self.__vertices[linha[0]] = [float(linha[2]),float(linha[3]) ,-1]#vertices['nome do vertice'] = ('coordenada x','coordenada y'))
        arq.close()

    def __le_links(self):
        arq = open(r'instancia1/links','r')
        while True:
            linha = arq.readline().split()
            if len(linha) == 0:
                break
            self.__links[linha[0]] = [linha[0],linha[2],linha[3],linha[5],linha[6],linha[7],linha[8],[]] #  links['nome do link'] = ( ( 'nome primeiro nó','nome segundo nó'),[] -> lista de modulos)
            i = 10
            while i <len(linha)-1:
                self.__links[linha[0]][7].append([float(linha[i]),float(linha[i+1])]) #links['nome do link'][1].append(('capacidade do modulo','custo do modulo'))
                i+=2
        arq.close()

    def __le_demands(self):
        arq = open(r'instancia1/demands')
        while True:
            linha = arq.readline().split()
            if len(linha) == 0:
                break
            self.__demands[linha[0]]=[linha[2],linha[3],linha[6]] #demands['nome da demanda'] = (('nome do nó de partida','nome do nó destino') ,'tamanho da demanda' )
        arq.close()

    def __gera_lista_nos(self):
        c = 0
        for i in self.__vertices:
            self.__vertices[i][2]=c
            self.nos.append(no(i,self.__vertices[i][0],self.__vertices[i][1]))
            c+=1

    def __gera_lista_arestas(self):
        for i in self.__links:
            T = []
            for j in self.__links[i][7]:
                T.append(modulo(float(j[0]),float(j[1])))
            self.E.append(link(int(self.__vertices[self.__links[i][1]][2]), int(self.__vertices[self.__links[i][2]][2]),self.__links[i][1],self.__links[i][2],i,float(self.__links[i][3]),float(self.__links[i][4]),float(self.__links[i][5]),float(self.__links[i][6]),T))

    def __gera_lista_demandas(self):
        c = 0
        for i in self.__demands:
            self.D.append(demanda(self.__vertices[self.__demands[i][0]][2],self.__vertices[self.__demands[i][1]][2],float(self.__demands[i][2]),i))

    def __init__(self):
        self.__le_demands()
        self.__le_links()
        self.__le_vertices()
        self.__gera_lista_nos()
        self.__gera_lista_arestas()
        self.__gera_lista_demandas()
