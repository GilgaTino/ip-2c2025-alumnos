# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global items, n, i, j
    #condicion para retornar "done":True, cuando haya recorrido la lista entera.   
    if i >= n:
        return {"a": 0, "b": 0, "swap": False, "done": True}

    # comenzar la inserción para items[i]
    if j is None:
        j = i
        return {"a": j-1, "b": j, "swap": False, "done": False}

    #pongo las condiciones para el swap y voy disminuyendo j hasta llegar al inicio de la lista, swapeando cuando corresponda.
    a = j-1
    b = j
    if j > 0 and items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap=True
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}

    # ya no hay más desplazamientos para este i
    i += 1
    j = None
    return {"a": 0, "b": 0, "swap": False, "done": False}
