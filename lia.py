import os
import subprocess
import random
import unicodedata

# ------------------ CONFIG ------------------
HOME = os.path.expanduser("~")
RUTA_MUSICA = os.path.join(HOME, "Música")
FORMATOS_AUDIO = (".mp3", ".wav", ".flac", ".ogg")

# ------------------ NORMALIZAR TEXTO ------------------
def limpiar(texto):
    texto = texto.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')

# ------------------ MÓDULO DE CHISTES ------------------
def obtener_chiste():
    chistes = [
        "¿Por qué la computadora fue al médico? Porque tenía un virus.",
        "¿Qué hace una abeja en el gimnasio? Zum-ba.",
        "¿Por qué los programadores confunden Halloween y Navidad? Porque OCT 31 es igual a DEC 25.",
        "¿Cuál es el café más peligroso? El ex-preso.",
        "¿Qué hace un mudo bailando? Una mudanza.",
        "¿Por qué los espejos no utilizan WhatsApp? Porque se reflejan en el pasado."
    ]
    return random.choice(chistes)

# ------------------ HABLAR ------------------
def hablar(texto):
    subprocess.run([
        "pico2wave", "-l=es-ES", "-w=temp.wav", texto
    ])
    os.system("aplay temp.wav")

# ------------------ ABRIR APP ------------------
def abrir_app(comando):
    subprocess.Popen(
        comando,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

# ------------------ EXPLORADOR INTELIGENTE ------------------
def abrir_explorador(carpeta=""):
    rutas = {
        "descargas": "Descargas",
        "documentos": "Documentos",
        "musica": "Música",
        "videos": "Videos",
        "imagenes": "Imágenes"
    }

    if carpeta == "":
        destino = HOME
    else:
        carpeta = limpiar(carpeta)
        destino = os.path.join(HOME, rutas.get(carpeta, carpeta))

    abrir_app(["xdg-open", destino])
    return f"Abriendo {carpeta if carpeta else 'inicio'}"

# ------------------ MÚSICA ------------------
def reproducir_todo():
    try:
        archivos = [
            os.path.join(RUTA_MUSICA, f)
            for f in os.listdir(RUTA_MUSICA)
            if f.lower().endswith(FORMATOS_AUDIO)
        ]

        if not archivos:
            return "No hay música"

        abrir_app(["cvlc"] + archivos)
        return "Reproduciendo toda tu música"
    except:
        return "Error al reproducir música"

# ------------------ RESPUESTAS ------------------
respuestas = {
    "hola": "Hola, ¿cómo has estado?",
    "bien": "Me alegra mucho escuchar eso",
    "mal": "Lo siento, espero que mejores",
    "quien eres": "Soy tu asistente tipo Jarvis, listo para ayudarte",
    "adios": "Hasta luego",
    "salir": "Hasta luego"
}

# ------------------ LOOP ------------------
while True:
    entrada = input("Adm: ")
    cmd = limpiar(entrada)

    # -------- CHISTE --------
    if "chiste" in cmd:
        hablar(obtener_chiste())

    # -------- ABRIR APPS --------
    elif "firefox" in cmd and "cierra" not in cmd:
        hablar("Abriendo Firefox")
        abrir_app(["firefox"])

    elif "code" == cmd:
        hablar("Abriendo VS Code")
        abrir_app(["code"])

    elif "vlc" == cmd:
        hablar("Abriendo VLC")
        abrir_app(["vlc"])

    elif "explorador" in cmd:
        hablar(abrir_explorador())

    elif "abrir carpeta" in cmd:
        carpeta = cmd.replace("abrir carpeta", "").strip()
        hablar(abrir_explorador(carpeta))

    # -------- MÚSICA --------
    elif "reproducir todo" in cmd:
        hablar(reproducir_todo())

    # -------- CERRAR --------
    elif "cierra firefox" in cmd:
        hablar("Cerrando Firefox")
        abrir_app(["pkill", "-15", "firefox"])

    elif "cierra vlc" in cmd:
        hablar("Cerrando VLC")
        abrir_app(["pkill", "-15", "vlc"])

    elif "cierra explorador" in cmd:
        hablar("Cerrando explorador")
        abrir_app(["pkill", "-15", "nautilus"])

    elif "cierra code" in cmd:
        hablar("Cerrando VS Code")
        abrir_app(["pkill", "-15", "code"])

    # -------- RESPUESTAS --------
    elif cmd in respuestas:
        hablar(respuestas[cmd])

    else:
        hablar("No lo entiendo")

    if cmd in ["adios", "salir"]:
        break