import os
import subprocess
import random

# ------------------ MÓDULO DE CHISTES ------------------
def obtener_chiste():
    chistes = [
        "¿Por qué la computadora fue al médico? Porque tenía un virus.",
        "¿Qué hace una abeja en el gimnasio? Zum-ba.",
        "¿Por qué los programadores confunden Halloween y Navidad? Porque OCT 31 es igual a DEC 25.",
        "¿Cuál es el café más peligroso? El ex-preso.",
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas."
    ]
    return random.choice(chistes)


# ------------------ RESPUESTAS ------------------
respuestas = {
    "hola": "Hola, ¿cómo has estado?",
    "bien": "Me alegra mucho escuchar eso",
    "mal": "Lo siento, espero que mejores",
    "adios": "Que tenga un buen día",
    "salir": "Hasta luego",
    "firefox": "Abriendo el navegador Firefox",
    "code": "Abriendo el editor de código",
    "vscode": "Abriendo el editor de código",
    "vlc": "Abriendo el reproductor de musica",
    "sublimetext": "Abriendo el editor de código",
    "cierra code": "Cerrando el editor de código",
    "cierra sublimetext": "Cerrando el editor de código",
    "cierra firefox": "Cerrando el navegador mozila",
    "cierra vlc": "Cerrando el reproductor de musica",
    "quien eres":"Soy una asistete virtual que te puede ayudar en realizar ciertas tareas sencillas hasta que tenga mas acciones que en futuras verciones"
}

lia = ""

# ------------------ HABLAR ------------------
def hablar(texto):
    subprocess.run([
        "pico2wave",
        "-l=es-ES",
        "-w=temp.wav",
        texto
    ])
    os.system("aplay temp.wav")

# ------------------ LOOP ------------------
while True:
    entrada = input("Adm: ").lower()

    # -------- CHISTE --------
    if entrada == "chiste":
        hablar(obtener_chiste())

    # -------- RESPUESTAS NORMALES --------
    elif entrada in respuestas:
        hablar(respuestas[entrada])

    else:
        hablar("No lo entiendo")

    # -------- ACCIONES --------
    if entrada == "firefox":
        subprocess.Popen(["firefox"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

    if entrada == "cierra firefox":
        subprocess.Popen(["pkill", "-15", "firefox"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if entrada == "code" or entrada == "vscode":
        os.system("code")

    if entrada == "cierra code":
        subprocess.run(["pkill", "code"])

    if entrada == "sublimetext":
        os.system("subl")

    if entrada == "cierra sublimetext":
        subprocess.run(["pkill", "subl"])

    if entrada == "vlc":
        subprocess.Popen(["vlc"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if entrada == "cierra vlc":
        subprocess.Popen(["pkill", "vlc"])

    if entrada == "quien eres":
        hablar(respuestas[entrada])

    if entrada == "adios" or entrada == "salir":
        break