# 🤖 Lia - Asistente Virtual

![alt text](./imagen/image.png)

Lia es un asistente virtual en desarrollo diseñado para interactuar mediante comandos en consola, permitiendo automatizar tareas básicas y ofrecer una experiencia conversacional simple.

Actualmente se encuentra en fase beta, pero ya cuenta con instalación nativa en Linux mediante un script automático.

---

### 🚀 Características
- Apertura de aplicaciones (Firefox, VLC, VS Code, Sublime Text, etc.)
- Cierre de aplicaciones (limitación actual con VS Code)
- Conversación básica
- Generación de chistes
- Sistema de memoria:
    - Notas
    - Tareas
    - Recordatorios

---

### 💻 Compatibilidad
| Sistema Operativo | Estado |
| --- |---| 
| Linux| ✅ Soportado|
|Windows|	🚧 En desarrollo|

---

### ⚙️ Instalación
#### 🐧 Instalación automática (recomendada)

Clona el repositorio:

```
git clone https://github.com/tu-usuario/lia.git
cd lia
```

Ejecuta el instalador:

```
chmod +x install.sh
./install.sh
```

### 🔊 Soporte de voz en Linux

El instalador configura automáticamente Pico TTS para la síntesis de voz.

Si deseas instalarlo manualmente:
```
sudo apt-get install libttspico-utils libttspico-data
```

### 🎵 Control de música

Para controlar la reproducción de música:

```
sudo apt install playerctl -y
```

### 🧠 Uso de comandos
### ▶️ Abrir aplicaciones
```
abre
abrir
inicia
ejecuta
```
### ⏹️ Cerrar aplicaciones
```cierra
cerrar
apaga
termina
quita
```
### 📝 Sistema de memoria
### 💾 Guardar información
```
lia recuerda que color es [color]
lia guarda nota comprar cables
lia agrega tarea estudiar python
```

### 🔍 Consultar información
```
lia qué recuerdas
lia ver notas
lia ver tareas
```

### ❌ Eliminar información
```
lia olvida color
lia elimina [tarea 1]
lia elimina nota 2
```

### 🆕 Versión 1.1
#### Cambios y mejoras
- ✔️ Se añadieron múltiples formas de ejecutar comandos (más naturalidad).
- ✔️ Implementación de sistema de memoria (notas, tareas y recordatorios).

### ⚠️ Limitaciones actuales
- Problemas al cerrar VS Code.
- Interfaz limitada a consola.
- Conversación aún básica.

### 📌 Próximas mejoras
- Interfaz gráfica (GUI)
- Mejor procesamiento de lenguaje natural
- Compatibilidad completa con Windows
- Integración con más aplicaciones

### 📄 Licencia

Este proyecto está bajo la licencia MIT.

### 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar Lia:

1. Haz un fork del repositorio
2. Crea una nueva rama
3. Realiza tus cambios
4. Envía un pull request