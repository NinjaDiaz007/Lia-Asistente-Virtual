#!/bin/bash

APP_NAME="lia"
INSTALL_DIR="/opt/$APP_NAME"

echo "📦 Instalando $APP_NAME..."

# Crear carpeta
sudo mkdir -p $INSTALL_DIR

# Copiar archivos (limpio, sin basura)
sudo rsync -av --exclude='__pycache__' --exclude='*.pyc' ./ $INSTALL_DIR/

# Crear comando global
echo "⚙️ Creando comando global..."

sudo tee /usr/local/bin/$APP_NAME > /dev/null <<EOF
#!/usr/bin/env python3

import sys
sys.path.insert(0, "$INSTALL_DIR")

from core.assistant import iniciar

if __name__ == "__main__":
    iniciar()
EOF

# Permisos
sudo chmod +x /usr/local/bin/$APP_NAME

echo "✅ Instalación completada"
echo "👉 Ejecuta con: $APP_NAME"