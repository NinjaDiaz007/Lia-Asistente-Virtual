import os
import subprocess
from utils.helpers import abrir_app 
from utils.helpers import abrir_app_system
from config.settings import RUTAS

HOME = os.path.expanduser("~")

def abrir_explorador(carpeta=""):
    if carpeta == "":
        destino = HOME
    else:
        destino = os.path.join(HOME, RUTAS.get(carpeta, carpeta))

    abrir_app(["xdg-open", destino])
    return f"Abriendo {carpeta if carpeta else 'inicio'}"

# -------- ABRIR --------
def abrir_firefox():
    abrir_app(["firefox"])
    return "Abriendo Firefox"

def abrir_code():
    abrir_app(["code"])
    return "Abriendo VS Code"

def abrir_vlc():
    abrir_app(["vlc"])
    return "Abriendo VLC"

def abrir_brave():
    abrir_app_system("brave")
    return "Abriendo Brave"

def abrir_sublimetext():
    abrir_app(["subl"])
    return "Abriendo el editor de codigo"

def abrir_terminal():
    # detecta automáticamente terminal disponible
    for cmd in [["gnome-terminal"], ["konsole"], ["xterm"]]:
        try:
            abrir_app(cmd)
            return "Abriendo terminal"
        except:
            continue

    return "No encontré una terminal disponible"

# -------- CERRAR --------
def cerrar_firefox():
    try:
        # 1. Intento elegante (cerrar ventana)
        subprocess.Popen(
            ["wmctrl", "-c", "Firefox"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return "Cerrar Firefox normal"
    except:
        pass

    try:
        # 2. Señal suave
        abrir_app(["pkill", "-15", "firefox"])
        return "Cerrando Firefox suavemente"
    except:
        pass

    try:
        # 3. Forzado (último recurso)
        abrir_app(["pkill", "-9", "firefox"])
        return "Cerrando Firefox forzadamente"
    except:
        return "No se pudo cerrar Firefox"

def cerrar_code():
    abrir_app(["pkill", "-15", "code"])
    return "Cerrando VS Code"

def cerrar_vlc():
    abrir_app(["pkill", "-15", "vlc"])
    return "Cerrando VLC"

def cerrar_sublimetext():
    try:
        # 2. Señal suave
        abrir_app(["pkill", "-15", "subl"])
        return "Cerrando editor de codigo"
    except:
        pass

    try:
        # 3. Forzado (último recurso)
        abrir_app(["pkill", "-9", "subl"])
        return "Cerrando el editor de codigo"
    except:
        return "No se pudo cerrar Firefox"