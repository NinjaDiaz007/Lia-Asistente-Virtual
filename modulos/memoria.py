import json
import os

ARCHIVO_MEMORIA = "memoria.json"

# -------- CARGAR --------
def cargar_memoria():
    if not os.path.exists(ARCHIVO_MEMORIA):
        return {}

    with open(ARCHIVO_MEMORIA, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

# -------- GUARDAR --------
def guardar_memoria(memoria):
    with open(ARCHIVO_MEMORIA, "w") as f:
        json.dump(memoria, f, indent=4)

# -------- RECORDAR --------
def recordar(texto):
    memoria = cargar_memoria()

    if "que" in texto:
        try:
            clave, valor = texto.split(" que ", 1)[1].split(" es ")
            memoria[clave.strip()] = valor.strip()
            guardar_memoria(memoria)
            return f"Recordaré que {clave} es {valor}"
        except:
            return "No entendí qué guardar"

    return "Usa 'recuerda que X es Y'"

# -------- MOSTRAR --------
def ver_memoria():
    memoria = cargar_memoria()

    if not memoria:
        return "No tengo recuerdos aún"

    return ", ".join([f"{k} es {v}" for k, v in memoria.items()])

# -------- OLVIDAR --------
def olvidar(clave):
    memoria = cargar_memoria()

    if clave in memoria:
        del memoria[clave]
        guardar_memoria(memoria)
        return f"Olvidé {clave}"

    return "No encontré eso"

def registrar_uso(categoria, valor):
    memoria = cargar_memoria()

    if "preferencias" not in memoria:
        memoria["preferencias"] = {}

    if categoria not in memoria["preferencias"]:
        memoria["preferencias"][categoria] = {}

    if valor not in memoria["preferencias"][categoria]:
        memoria["preferencias"][categoria][valor] = 0

    memoria["preferencias"][categoria][valor] += 1

    guardar_memoria(memoria)


def obtener_preferencia(categoria):
    memoria = cargar_memoria()

    if "preferencias" not in memoria:
        return None

    if categoria not in memoria["preferencias"]:
        return None

    opciones = memoria["preferencias"][categoria]

    # devuelve el más usado
    return max(opciones, key=opciones.get)

# -------- USUARIO --------
def guardar_usuario(clave, valor):
    memoria = cargar_memoria()

    if "usuario" not in memoria:
        memoria["usuario"] = {}

    memoria["usuario"][clave] = valor
    guardar_memoria(memoria)

    return f"Guardé que tu {clave} es {valor}"


def obtener_usuario(clave):
    memoria = cargar_memoria()

    if "usuario" in memoria and clave in memoria["usuario"]:
        return f"Tu {clave} es {memoria['usuario'][clave]}"

    return "No tengo esa información"


# -------- TAREAS --------
def agregar_tarea(tarea):
    memoria = cargar_memoria()

    if "tareas" not in memoria:
        memoria["tareas"] = []

    memoria["tareas"].append(tarea)
    guardar_memoria(memoria)

    return f"Tarea agregada: {tarea}"


def ver_tareas():
    memoria = cargar_memoria()

    if "tareas" not in memoria or not memoria["tareas"]:
        return "No tienes tareas"

    lista = "\n".join([f"{i+1}. {t}" for i, t in enumerate(memoria["tareas"])])
    return f"Tus tareas son:\n{lista}"


def eliminar_tarea(numero):
    memoria = cargar_memoria()

    if "tareas" not in memoria or not memoria["tareas"]:
        return "No hay tareas"

    try:
        tarea = memoria["tareas"].pop(numero - 1)
        guardar_memoria(memoria)
        return f"Eliminé: {tarea}"
    except:
        return "Número inválido"
    
# -------- NOTAS --------
def agregar_notas(nota):
    memoria = cargar_memoria()

    if "nota" not in memoria:
        memoria["notas"] = []

    memoria["notas"].append(nota)
    guardar_memoria(memoria)

    return f"Notas agregada: {nota}"


def ver_notas():
    memoria = cargar_memoria()

    if "notas" not in memoria or not memoria["notas"]:
        return "No tienes notas"

    lista = "\n".join([f"{i+1}. {t}" for i, t in enumerate(memoria["notas"])])
    return f"Tus notas son:\n{lista}"


def eliminar_tarea(numero):
    memoria = cargar_memoria()

    if "notas" not in memoria or not memoria["notas"]:
        return "No hay notas"

    try:
        nota = memoria["notas"].pop(numero - 1)
        guardar_memoria(memoria)
        return f"Eliminé: {nota}"
    except:
        return "Número inválido"