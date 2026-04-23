from utils.helpers import limpiar, hablar
from config.settings import PALABRA_CLAVE
from modulos import musica, sistema, conversacion
from modulos import memoria

# ------------------ INTELIGENCIA ------------------
def detectar_intencion(cmd):
    abrir = ["abre", "abrir", "inicia", "ejecuta"]
    cerrar = ["cierra", "cerrar", "apaga", "termina", "quita"]

    apps = {
        "firefox": ["firefox", "navegador", "mozilla", "mozila"],
        "code": ["code", "vscode", "editor"],
        "vlc": ["vlc", "musica", "reproductor"],
        "terminal": ["terminal", "consola", "shell"],
        "sublimetext": ["sublimetext", "sub"]
    }

    accion = None
    aplicacion = None

    if any(p in cmd for p in abrir):
        accion = "abrir"
    elif any(p in cmd for p in cerrar):
        accion = "cerrar"

    for app, alias in apps.items():
        if any(a in cmd for a in alias):
            aplicacion = app
            break

    return accion, aplicacion


# ------------------ LOOP PRINCIPAL ------------------
def iniciar():
    while True:
        entrada = input(">> ")
        cmd = limpiar(entrada)

        # -------- CONVERSACIÓN --------
        if "chiste" in cmd:
            hablar(conversacion.obtener_chiste())
            continue

        if cmd in conversacion.respuestas:
            hablar(conversacion.respuestas[cmd])

            if cmd in ["adios", "salir"]:
                break
            continue

        # -------- REQUIERE PALABRA CLAVE --------
        if PALABRA_CLAVE not in cmd:
            continue

        cmd = cmd.replace(PALABRA_CLAVE, "").strip()

        if cmd == "":
            hablar("Te escucho")
            continue

        # -------- MÚSICA --------
        if "reproducir todo" in cmd or "reprodice todo" in cmd or "canciones" in cmd:
            hablar(musica.reproducir_todo())
            continue

        elif "pausa" in cmd or "pausar" in cmd:
            hablar(musica.controlar("pausa"))
            continue

        elif "continuar" in cmd or "reanudar" in cmd:
            hablar(musica.controlar("play"))
            continue

        elif "detener" in cmd:
            hablar(musica.controlar("detener"))
            continue

        elif "siguiente" in cmd:
            hablar(musica.controlar("siguiente"))
            continue

        elif "anterior" in cmd or "atras" in cmd:
            hablar(musica.controlar("anterior"))
            continue

        # -------- INTELIGENCIA (APPS) --------
        accion, app = detectar_intencion(cmd)

        if accion and app:

            if accion == "abrir":

                if app == "firefox":
                    memoria.registrar_uso("navegador", "firefox")
                    hablar(sistema.abrir_firefox())

                elif app == "code":
                    hablar(sistema.abrir_code())

                elif app == "vlc":
                    memoria.registrar_uso("musica", "vlc")
                    hablar(sistema.abrir_vlc())

                elif app == "terminal":
                    hablar(sistema.abrir_terminal())
                
                elif app == "sublimetext":
                    hablar(sistema.abrir_sublimetext())

            elif accion == "cerrar":

                if app == "firefox":
                    hablar(sistema.cerrar_firefox())

                elif app == "code":
                    hablar(sistema.cerrar_code())

                elif app == "vlc":
                    hablar(sistema.cerrar_vlc())

                elif app == "sublimetext":
                    hablar(sistema.cerrar_sublimetext())

            continue

        # -------- EXPLORADOR --------
        if "explorador" in cmd:
            hablar(sistema.abrir_explorador())
            continue

        elif "abrir carpeta" in cmd:
            carpeta = cmd.replace("abrir carpeta", "").strip()
            hablar(sistema.abrir_explorador(carpeta))
            continue

        # -------- MEMORIA --------
        if "recuerda que" in cmd:
            hablar(memoria.recordar(cmd))
            continue
            #return

        elif "que recuerdas" in cmd:
            hablar(memoria.ver_memoria())
            continue #return

        elif "olvida" in cmd:
            clave = cmd.replace("olvida", "").strip()
            hablar(memoria.olvidar(clave))
            continue #return

        if "abre navegador" in cmd:
            pref = memoria.obtener_preferencia("navegador")

            if pref == "firefox":
                hablar(sistema.abrir_firefox())
            else:
                hablar("No tengo navegador preferido aún")

        # -------- USUARIO --------
        if "mi nombre es" in cmd:
            nombre = cmd.replace("mi nombre es", "").strip()
            hablar(memoria.guardar_usuario("nombre", nombre))
            continue

        elif "como me llamo" in cmd:
            hablar(memoria.obtener_usuario("nombre"))
            continue

        elif "mi color favorito es" in cmd:
            color = cmd.replace("mi color favorito es", "").strip()
            hablar(memoria.guardar_usuario("color", color))
            continue


        # -------- TAREAS --------
        elif "agrega tarea" in cmd:
            tarea = cmd.replace("agrega tarea", "").strip()
            hablar(memoria.agregar_tarea(tarea))
            continue

        elif "ver tareas" in cmd:
            hablar(memoria.ver_tareas())
            continue

        elif "elimina tarea" in cmd:
            try:
                numero = int(cmd.replace("elimina tarea", "").strip())
                hablar(memoria.eliminar_tarea(numero))
            except:
                hablar("Dime el número de la tarea")
            continue

        # -------- NOTAS --------
        elif cmd.startswith("agrega nota") or cmd.startswith("agrega notas"):
            partes = cmd.split(" ", 2)

            if len(partes) < 3:
                hablar("Dime qué nota agregar")
            else:
                nota = partes[2]
                hablar(memoria.agregar_notas(nota))

            continue

        # -------- FALLBACK --------
        hablar("No entendí el comando")