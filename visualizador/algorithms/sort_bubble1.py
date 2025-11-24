# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items=[]
n=0
j=0
i=0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = n-1
    j = 0

def step():
    global items, n, i, j
    # Condicion para que el algoritmo devuelva "done": True. (termine),si i==0 termine de ordenar
    if i<1:
        return {"done":True}
    a=j
    b=j+1
    swap=False
    #comparo desde items[0] con el siguiente en la lista y hago swap si corresponde 
    if items[a]>items[b]:
        items[a],items[b]=items[b],items[a]
        swap=True
    #avanzo j 
    j+=1
    #si j llega al final de la lista, vuelvo a empezar desde 0 y disminuyo i
    if j>=i:
        i-=1
        j=0
    return {"a": a, "b": b, "swap": swap, "done": False}

    
    
    
    
    
    
    
    
    
    
    
    # TODO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.
    #return {"done": True}
