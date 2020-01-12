import os
import numpy as np
import networkx as nx 


print(' TRABAJO 1: MATRICES DE ADYACENCIA DE GRAFOS\n')

def menu():
    os.system('clear')
    print(' ------------------------------- ')
    print('1. Ingresar Grafo')
    print('2. Mostrar Matriz de Adyacencia')
    print('3. Verificar si es conexo o no')
    print('4. Caminos')
    print('5. Dijkstra')
    print('6. Salir')
    print(' ------------------------------- ')


class Grafo:
    # Se resetea los vertices y matriz para ser ingresado nuevamente
    def __init__(self):
        self.vertices = []
        self.aristas = []
        self.matriz = [[None] * 0 for i in range(0)]

    # Se resetea los vertices y matriz para ser ingresado nuevamente
    def reset(self):
        self.vertices = []
        self.aristas = []
        self.matriz = [[None] * 0 for i in range(0)]
    
    # Verifica si el usuario que ingresó el vertice existe o no en opcion 1 (aristas) y 5 del menu
    def comprobacion_vertice(self, vertice):
      for i in self.vertices:
        if(i == vertice):
          return True
      return False

    # Verifica si el usuario ingresó el peso de una arista correctamente
    def comprobacion_tipo(self, x):
      try:
            x = int(x)
            return True
      except ValueError:
            return False
    
    # Verifica si el vertice ingresado ya está en la matriz
    def isVertice(self, v):
        if (self.matriz.count(v) == 0):
            return False
        return True
      
    
      
    # Añade un vertice a la matriz
    def addVertice(self, v):
        if (self.isVertice(v)):
            return False
        self.vertices.append(v)
        
        # Preparando la matriz de adyacecia
        
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas + 1) for i in range(columnas + 1)]

        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        self.matriz = matriz_aux
        return True

    #Añade una arista con su respectivo peso
    def addArista(self, inicio, fin, peso):
        if not (self.isVertice(inicio) or not (self.isVertice(fin))):
            return False

        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = peso
        # Para grafos no dirigidos
        self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = peso
        return True

    # Añade un arista con su respectivo peso para ocupar en dijkstra
    def addArista2(self, a):
      self.aristas.append(a)
      
    # Imprime la matriz del Grafo
    def imprimir_matriz(self, m):
        cadena = "\n"

        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])

        cadena += "\n" + ("        -" * len(m))

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if ((f == c) and (m[f][c] is None or m[f][c] == 0)):
                    cadena += "\t" + "0"
                else:
                    if (m[f][c] is None):
                        cadena += "\t" + "0"
                    #           elif(math.isinf(m[f][c])):
                    #             cadena += "\t" + "∞"
                    else:
                        cadena += "\t" + "1"

        cadena += "\n"
        print(cadena)
    
    #revisa si es conexo o no el grafo
    def isConexo(self):
        filas = columnas = len(self.matriz)
        #Matriz de peso para el calculo
        matriz_aux = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (self.matriz[f][c] is None):
                    matriz_aux[f][c] = 0
                else:
                    matriz_aux[f][c] = int(self.matriz[f][c])
        # Matriz identidad
        matriz_identidad = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (f == c):
                    matriz_identidad[f][c] = 1
                else:
                    matriz_identidad[f][c] = 0
        ma = np.matrix(matriz_aux)
        C = np.matrix(matriz_identidad)
        for i in range(filas - 1):
            C_aux = ma
            while(i > 0):
                C_aux = C_aux * ma
                i = i - 1
            C = C + C_aux
        
        #Pregunto si hay algun 0
        if(np.any(C == 0)):
            return False
        else:
            return True
          
          
    #caminos de largo n para el grafo
    def Caminos(self, caminos):
        filas = columnas = len(self.matriz)
        #Matriz de adyacencia con numeros enteros 1 y 0
        matriz = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (self.matriz[f][c] is None):
                    matriz[f][c] = 0
                else:
                    matriz[f][c] = 1
        # Matriz identidad
        matriz_identidad = [[0] * (filas) for i in range(columnas)]
        for f in range(filas):
            for c in range(columnas):
                if (f == c):
                    matriz_identidad[f][c] = 1
                else:
                    matriz_identidad[f][c] = 0
        if(int(caminos) > int(filas)):
            #No puede existir caminos de ese largo para la matriz dada
            print("No existen caminos de ese largo para el grafo dado")
        elif(caminos == 0):
            for f in range(filas):
                for c in range(columnas):
                    if(matriz_identidad[f][c] != 0):
                        print(self.vertices[f] + "->" + self.vertices[c] + "  Cantidad de caminos: " + str(matriz_identidad[f][c]))
        elif(caminos == 1):
            for f in range(filas):
                for c in range(columnas):
                    if(int(matriz[f][c]) != 0):
                        print(self.vertices[f] + "->" + self.vertices[c] + "  Cantidad de caminos: " + str(matriz[f][c]))
        else:
            matriz = matriz_aux = np.matrix(matriz)
            i = 0
            while(i < int(caminos)-1):
                matriz = matriz * matriz_aux
                i = i + 1
            matriz = matriz.tolist()
            #print(matriz)  mostramos matriz para ejemplo
            for f in range(filas):
                for c in range(columnas):
                    if(int(matriz[f][c]) != 0):
                        print(self.vertices[f] + "->" + self.vertices[c] + "  Cantidad de caminos: " + str(matriz[f][c]))
  
  
    def dijkstra(self, v_inicial):
        if(self.vertices.count(v_inicial) == 0):
            print("El nodo que ha ingresado no pertenece al grafo")
        else:
            filas = columnas = len(self.matriz)
            #Matriz de peso con enteros
            matriz = [[0] * (filas) for i in range(columnas)]
            for f in range(filas):
                for c in range(columnas):
                    if(self.matriz[f][c] is None):
                        matriz[f][c] = 0
                    else:
                        matriz[f][c] = int(self.matriz[f][c])

            #Creo un array de numpy para analizar la matriz mas facilmente
            matriz = np.array(matriz)
            #Creo el grafico de la libreria networkx para usar sus metodos (Dijkstra)
            G = nx.from_numpy_matrix(matriz, create_using=nx.DiGraph())
            pred, dist = nx.dijkstra_predecessor_and_distance(G, self.vertices.index(v_inicial))
            dist = dist.items()
            # print(pred) #Antecesores como diccionario
            # print(pred.items()) #Antecesores como arreglo
            for i in dist:
                #Rearmando la ruta
                #Codigo del rearme de ruta (In progress...)
                
                #Distancias (working...)
                print("Distancia menor de " + v_inicial + "->" + self.vertices[i[0]] + ": " + str(i[1]))

        
        
    
Grafo = Grafo()
while True:
    menu()
    opcionMenu = input('Ingrese una opcion>> ') 
    if (opcionMenu == '1'):
        os.system("clear")
        validacion = 1 # Variable en la cual valida si el usuario ingresó correctamente o no
        while(validacion == 1):
          validacion2 = 1 # Variable en la cual valida si se ha detectado un error en el ingreso de datos
          Grafo.reset()
          vertices = input('Ingrese vertices separados por espacio>> ')
          vertices = vertices.split(" ")
          for vertice in vertices:
              Grafo.addVertice(vertice)
          os.system("clear")
          aristas_peso = input('Ingrese aristas y su peso. Ej: a,b,2 b,c,3>> ')
          aristas_peso = aristas_peso.split(" ")
          for a in aristas_peso:
            a = a.split(",")
            Grafo.addArista2(a)
            if(len(a)==3):
              if(Grafo.comprobacion_vertice(a[0]) and Grafo.comprobacion_vertice(a[1])):
                if(Grafo.comprobacion_tipo(a[2])):
                  Grafo.addArista(a[0], a[1], a[2])  #Si en caso que todo corre sin ningun error
                else:
                   validacion2 = 2 #En caso de que el usuario comete un error
              else:
                validacion2 = 2 #En caso de que el usuario comete un error
            else:
              validacion2 = 2 #En caso de que el usuario comete un error
          if(validacion2 == 2):
            print(" Mal ingreso de datos, revisa y vuelve a intentar ...")
          else:
            validacion = 2
            print("Datos ingresados correctamente")
        input("Presione ENTER para continuar...")
        
    elif (opcionMenu == '2'):
        os.system("clear")
        Grafo.imprimir_matriz(Grafo.matriz)
        input("Presione ENTER para continuar...")
        
    elif (opcionMenu == '3'):
        os.system("clear")
        if (Grafo.isConexo()):
            print("El grafo es conexo")
        else:
            print("El grafo no es conexo")
        input("Presione ENTER para continuar...")
        
    elif(opcionMenu == '4'):
        caminos = input("Ingrese el largo que desea ver: ")
        os.system("clear")
        print("Caminos de largo " + str(caminos))
        Grafo.Caminos(int(caminos))
        input("Presione ENTER para continuar...")
        
    elif(opcionMenu == '5'):
      validacion = 1 # Variable en la cual valida si el usuario ingresó correctamente o no
      while(validacion == 1):
        vertice_inicial = input("Ingrese el vertice que quieras iniciar (que sea existente): ")
        if(Grafo.comprobacion_vertice(vertice_inicial)):
            validacion = 2
        else:
          print("Mal ingreso de vertice ya que no se encuentra en el grafo, vuelve a ingresar")
      Grafo.dijkstra(vertice_inicial)
      input("Presione ENTER para continuar...")
    elif (opcionMenu == '6'):
        break  