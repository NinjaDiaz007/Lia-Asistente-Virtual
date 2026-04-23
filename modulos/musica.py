import os
import subprocess
from utils.helpers import abrir_app

HOME = os.path.expanduser("~")
RUTA_MUSICA = os.path.join(HOME, "Música")
FORMATOS = (".mp3", ".wav", ".flac", ".ogg")

def reproducir_todo():
    try:
        archivos = [
            os.path.join(RUTA_MUSICA, f)
            for f in os.listdir(RUTA_MUSICA)
            if f.lower().endswith(FORMATOS)
        ]

        if not archivos:
            return "No hay música"

        abrir_app(["cvlc"] + archivos)
        return "Reproduciendo música"
    except:
        return "Error al reproducir"

def controlar(comando):
    comandos = {
        "pausa": ["playerctl", "play-pause"],
        "play": ["playerctl", "play"],
        "detener": ["playerctl", "stop"],
        "siguiente": ["playerctl", "next"],
        "anterior": ["playerctl", "previous"]
    }

    if comando in comandos:
        abrir_app(comandos[comando])
        return f"{comando} ejecutado"

    return "Comando no válido"