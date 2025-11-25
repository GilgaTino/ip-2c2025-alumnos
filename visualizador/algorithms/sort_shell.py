# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
# Implementación paso-a-paso de Shell sort pensada para un visualizador.
elementos = []
n = 0

brechas = []   # lista de gaps a procesar
brecha = 0     # gap actual
i = 0          # índice del elemento que inserta en la pasada gapped
j = None       # cursor para desplazar hacia la izquierda dentro de la misma brecha
fase = "cambio"  # "cambio" | "procesando"

def init(vals):
    global elementos, n, brechas, brecha, i, j, fase
    elementos = list(vals)
    n = len(elementos)
    # Secuencia simple de gaps: n//2, //2, ...
    brechas = []
    g = n // 2
    while g > 0:
        brechas.append(g)
        g //= 2
    brecha = 0
    i = 0
    j = None
    fase = "cambio"

def step():
    global elementos, n, brechas, brecha, i, j, fase

    #para listas ya ordenadas o de tamaño 0 o 1
    if n <= 1:
        return {"a": 0, "b": 0, "swap": False, "done": True}

    # Si no hay brechas pendientes, terminamos
    if fase == "cambio":
        if not brechas:
            return {"a": 0, "b": 0, "swap": False, "done": True}
        # tomar siguiente gap, con brechas.pop(0),tomo el valor y lo quito de la lista en un paso
        brecha = brechas.pop(0)
        i = brecha
        j = None
        fase = "procesando"
        # mostrar la primera comparación para la nueva brecha
        return {"a": i - brecha, "b": i, "swap": False, "done": False}

    # Fase de procesado para la brecha actual
    if fase == "procesando":
        # Si ya recorrimos todos los i para esta brecha, paso a cambio para tomar la siguiente
        if i >= n:
            fase = "cambio"
            return {"a": 0, "b": 0, "swap": False, "done": False}

        # Si aún no comenzamos con el i actual, inicializamos j
        if j is None:
            j = i
            # mostrar comparación inicial entre j-brecha y j
            return {"a": j - brecha, "b": j, "swap": False, "done": False}

        # Comparar y, si corresponde, hacer swap adyacente a distancia 'brecha'
        a = j - brecha
        b = j
        if a >= 0 and elementos[a] > elementos[b]:
            elementos[a], elementos[b] = elementos[b], elementos[a]
            # mover cursor hacia la izquierda para seguir insertando este elemento
            j -= brecha
            # si j queda menor que brecha, esto indica que la inserción terminó en el borde;
            # la próxima llamada detectará j<brecha y avanzará i.
            return {"a": a, "b": b, "swap": True, "done": False}
        else:
            # no se requiere más desplazamiento para este i; pasar al siguiente i
            i += 1
            j = None
            return {"a": 0, "b": 0, "swap": False, "done": False}
