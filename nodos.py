class Nodo:
    def __init__(self,fila,columna,valor):
        self.valor=valor

        self.fila=fila
        self.columna=columna
        self.derecha = None
        self.izquierda = None
        self.arriba = None  
        self.abajo = None
        
        self.final = None
        self.temporal = None
        self.revisado = False
      
        self.x = None
        self.y = None

        self.star = 1
        self.finish = 0

class nodoEncabezado:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None
    