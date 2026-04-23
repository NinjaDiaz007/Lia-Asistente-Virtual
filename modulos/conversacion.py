import random

def obtener_chiste():
    return random.choice([
        "¿Por qué la computadora fue al médico? Porque tenía un virus.",
        "¿Qué hace una abeja en el gimnasio? Zum-ba.",
        "¿Cuál es el café más peligroso? El ex-preso."
    ])

respuestas = {
    "hola": "Hola, ¿cómo has estado?",
    "bien": "Me alegra escuchar eso",
    "mal": "Espero que mejores",
    "quien eres": "Soy tu asistente tipo Jarvis",
    "adios": "Hasta luego",
    "salir": ""
}