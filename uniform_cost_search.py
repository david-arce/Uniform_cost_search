import matriz_random
import grafica

class TreeNode:
    def __init__(self, cost, position, padre):
        self.cost = cost
        self.hijos = []
        self.position = position
        self.nodoPadre = padre
        self.raiz = False
        self.cambiado = False
        self.posicion_anterior_de_mi_padre = None
        self.completo = False
        self.matriz = matriz
        
    #comparamos la posicion de un nodo para saber si ya llegamos a la meta
    def is_goal(self, meta):
        if self.position[0] == meta[0] and self.position[1] == meta[1]:
            return True
        return False
    
    #verificamos si al expandir tengo hijos, si no tengo hijos ya estoy completo
    def i_have_childrens(self):
        if not self.hijos:
            self.completo = True
            return False
        return True
    
    #obtienen los nodos y coordenadas de mi ruta hasta la raiz
    def get_recorrido(self):
        if self is None:
            return nodos_recorridos, coordenadas
        nodos_recorridos = [self]
        coordenadas = [self.position]
        while not self.raiz:
            nodos_recorridos.append(self.nodoPadre)
            coordenadas.append(self.nodoPadre.position)
            self = self.nodoPadre
        coordenadas.reverse()
        return nodos_recorridos, coordenadas
    
    #pregunta si mi hijo es el menor para ver si seguir por ahi o cambiar de nodo
    def mi_hijo_es_el_mejor(self, nodo):
        for hijo in self.hijos:
            if nodo == hijo:
                return True
        return False
    
    #me retorna el numero de hijo que soy de mi padre
    def indice_en_padre(self):
        if self.nodoPadre is not None:
            for i, hijo in enumerate(self.nodoPadre.hijos):
                if hijo is self:
                    return i
        return None
    
# construir es uns funcion recursiva que va creando el arbol y retorna las 
# coordenadas de la matriz con menor costo
def construir(matriz, nodo, meta):
    if nodo == None:
        return "Nodo vacio"
    
    if not coordenada_en_matriz(matriz, meta[0], meta[1]):
        return "La meta no existe dentro de la matriz"
    
    if matriz[meta[0]][meta[1]] == 0:
        return "Nunca llegaras a la meta porque no puedes atravezar la pared"

    if nodo.is_goal(meta):
        #si llegamos a la meta retorno las coordenadas para recorrer la matriz
        _, coordenadas = nodo.get_recorrido()
        return nodo.cost, coordenadas
    
    #si no es meta expando el nodo
    _, coordenadas = nodo.get_recorrido()
    nodo.matriz = poner_en_cero_matriz(matriz, coordenadas)
    nodo.hijos = expandir(nodo.matriz, nodo)
    
    #obtengo la informacion del nodo siguiente (el de menor costo)
    nodos_ordenados = organizar_nodos_desde_nodo(raiz)
    mi_recorrido, _ = nodo.get_recorrido()
    nodo_siguiente = get_best_node(mi_recorrido, nodos_ordenados)
    
    #si no tengo hijos es porque ya no hay recorrido entonces cambio de nodo
    if not nodo.i_have_childrens(): 
        if not nodo_siguiente:
            return "Es imposible llegar a la meta"
        return construir(matriz, nodo_siguiente[0], meta)
    
    #verifico si mi hijo es el mejor para asi no hacer cambios al arbol
    if nodo.mi_hijo_es_el_mejor(nodo_siguiente[0]):
        nodo.completo = True
        if nodo_siguiente[0].cambiado:
            revertir(nodo_siguiente[0])
        return construir(matriz, nodo_siguiente[0], meta)
    
    #cambia la posicion del padre por su mejor hijo
    acomodar_arbol(nodo) 
    
    #si el nodo siguiente fue un nodo cambiado (osea reemplaze al 
    # padre por su mejor hijo) lo revierto
    if nodo_siguiente[0].cambiado:
        revertir(nodo_siguiente[0])
        
    return construir(matriz, nodo_siguiente[0], meta)

#cada nodo guarda su matriz para saber por donde no devolverse, 
# en este caso donde haya un cero
def poner_en_cero_matriz(matriz, coordenadas_a_cero):
    nueva_matriz = [fila[:] for fila in matriz]

    for fila, columna in coordenadas_a_cero:
        if 0 <= fila < len(nueva_matriz) and 0 <= columna < len(nueva_matriz[0]):
            nueva_matriz[fila][columna] = 0

    return nueva_matriz

#cambio el padre por su mejor hijo
def acomodar_arbol(nodo):
    i = nodo.indice_en_padre()
    if i == None:
        return
    
    mejor_hijo = min(nodo.hijos, key=lambda hijo: hijo.cost) 
    indice_mejor_hijo = nodo.hijos.index(mejor_hijo)

    nodo.nodoPadre.hijos[i] = nodo.hijos[indice_mejor_hijo]
    nodo.hijos[indice_mejor_hijo].cambiado = True
    nodo.hijos[indice_mejor_hijo].posicion_anterior_de_mi_padre = i
    
#si ahora un nodo cambiado es el mejor lo revierto para continuar
def revertir(nodo):
    i = nodo.posicion_anterior_de_mi_padre
    nodo.nodoPadre.nodoPadre.hijos[i] = nodo.nodoPadre
    nodo.nodoPadre.completo = True   
   

# Realiza un recorrido DFS para recoger todos los nodos en una lista 
# y despues los acomoda por menor costo
def organizar_nodos_desde_nodo(nodo):
    def recorrido_dfs(nodo, nodos):
        if nodo is None:
            return
        nodos.append(nodo)
        for hijo in nodo.hijos:
            recorrido_dfs(hijo, nodos)

    nodos = []
    recorrido_dfs(nodo, nodos)
    nodos.sort(key=lambda nodo: nodo.cost)  # Organiza la lista de nodos de menor a mayor
    return nodos   

#retorna una lista con los valores de nodos_creados_ordenados 
# sin los valores de mi_recorrido, ademas elimina los nodos que esten completos
def get_best_node(mi_recorrido, nodos_creados_ordenados):
    nueva_lista = [valor 
                   for valor in nodos_creados_ordenados
                   if valor not in mi_recorrido and not valor.completo]
    return nueva_lista

#verifica que la meta se encuentre dentro d ela matriz
def coordenada_en_matriz(matriz, fila, columna):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])  

    if 0 <= fila < num_filas and 0 <= columna < num_columnas:
        return True
    else:
        return False
    
#retorna los hijos de un nodo
def expandir(matriz, padre):
    children = []
    i = padre.position[0]
    j = padre.position[1]
    costo_acumulado = padre.cost
    if i-1 >= 0:
        if matriz[i-1][j] != 0:
            nodo = TreeNode(matriz[i-1][j] + costo_acumulado, #costo acumulado
                            [i-1,j], #posicion en la matriz
                            padre) # nodo padre
            children.append(nodo)
    if j+1 < len(matriz[0]):
        if matriz[i][j+1] != 0:
            nodo = TreeNode(matriz[i][j+1] + costo_acumulado,
                            [i,j+1],
                            padre)
            children.append(nodo)
    if i+1 < len(matriz):
        if matriz[i+1][j] != 0:
            nodo = TreeNode(matriz[i+1][j] + costo_acumulado,
                            [i+1,j],
                            padre)
            children.append(nodo)
    if j-1 >= 0:
        if matriz[i][j-1] != 0:
            nodo = TreeNode(matriz[i][j-1] + costo_acumulado,
                            [i,j-1],
                            padre)
            children.append(nodo)
    matriz[i][j] = 0
    return children


#----------------------------------     PRUEBAS     ---------------------------------
# matriz = [
#     # [1, 1, 3, 1, 1, 1, 1, 1],
#     # [1, -2, 0, 0, -2, 0, 0, 1],
#     # [1, 0, 1, 1, 1, 0, 0, 1],
#     # [1, 0, 1, 0, 0, 0, 1, 1],
#     # [1, -2, 1, 3, 1, 1, 1, 1],
    
#     [1, 1, 1, 1, 0, -2, 0, 1],
#     [0, 0, 1, 1, 1, 1, -2, 1],
#     [-2, 0, 3, 0, 0, 1, 1, 1],
#     [1, 1, 0, 1, 0, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 0, 3]
  
# ]

# Tamaño de la matriz
filas = 5
columnas = 8

# Número a colocar en posiciones aleatorias
#muriel = 4, coraje = 5 (esto solo para pintar la interfaz)
numero = [3, -2, 0, 4, 5]

# Cantidad de veces que se debe colocar el número
cantGatos = 2
cantAmos = 3
cantObstaculos = 11
muriel = 1
coraje = 1

# Inicializar una matriz con unos que son los espacios en blanco
matriz = [[1] * columnas for _ in range(filas)]

# Llena la matriz con el número en posiciones aleatorias
matriz_aleatoria = matriz_random.llenar_matriz(matriz, numero, cantGatos, cantAmos, cantObstaculos, muriel, coraje)

#cambiar los numeros 4 y 5 por 1
for row in range(len(matriz_aleatoria)):
    for col in range(len(matriz_aleatoria[0])):
        if matriz_aleatoria[row][col] == 4:
            finish = [row,col]
            matriz_aleatoria[row][col] = 1
        if matriz_aleatoria[row][col] == 5:
            start = [row,col]
            matriz_aleatoria[row][col] = 1
            

raiz = TreeNode(0, start, None)
# raiz = None
raiz.raiz = True

dato = construir(matriz_aleatoria, raiz, finish)

# Extraer el costo
costo = dato[0]

# Convertir la lista anidada en una lista de tuplas
nodos_recorridos = [tuple(sublista) for sublista in dato[1]]

print('Inicio:', start)
print('Meta:', finish)
print('Costo: ',costo)
print('Nodos recorridos: ',nodos_recorridos)
print('------------Matriz----------------')
for i in matriz_aleatoria:
    print(i)
    
    
grafica.start_visualization(matriz_aleatoria, start, finish, nodos_recorridos)


