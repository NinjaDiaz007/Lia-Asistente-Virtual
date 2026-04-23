import os
import subprocess
import unicodedata

def limpiar(texto):
    texto = texto.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')

def hablar(texto):
    subprocess.run(["pico2wave", "-l=es-ES", "-w=temp.wav", texto])
    subprocess.run(["aplay", "temp.wav"])

def abrir_app(comando):
    subprocess.Popen(
        comando,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

def abrir_app_system(com):
    os.system(com)