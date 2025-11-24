# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase

    # Condicion para que el algoritmo devuelva "done": True. (termine)
    if n <= 1 or i >= n - 1:
        return {"done": True}

    # Fase de búsqueda: comparar j con min_idx
    if fase == "buscar":
        if j < n:
            a = min_idx
            b = j
            # actualizo min_idx cuadno encontro un valor menor
            if items[j] < items[min_idx]:
                min_idx = j
            j += 1
            return {"a": a, "b": b, "swap": False, "done": False}
        else:
            # en else, j>n, osea recorri la lista entera, paso a swap
            fase = "swap"

    # Fase de swap: realizar (si corresponde) el intercambio entre i y min_idx
    if fase == "swap":
        a = i
        b = min_idx
        swap = False
        # condicion que min_idx sea diferente de i para hacer el swap,sino no hace nada.
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap = True
        # avanzo i para la siguiente iteracion y reinicio j y min_idx
        i += 1
        min_idx = i
        j = i + 1
        fase = "buscar"
        # si ya estamos en el ultimo i, marcar "done" True.
        if i >= n - 1:
            return {"a": a, "b": b, "swap": swap, "done": True}
        return {"a": a, "b": b, "swap": swap, "done": False}















    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    return {"done": True}

