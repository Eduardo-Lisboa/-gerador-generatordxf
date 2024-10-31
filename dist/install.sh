#!/bin/bash

# Caminho para o diretório de instalação
INSTALL_DIR="$HOME/GeradorDePecasDXF"

# Criar o diretório de instalação
mkdir -p "$INSTALL_DIR"

# Copiar os arquivos para o diretório de instalação
cp maquina "$INSTALL_DIR/"
cp icon.png "$INSTALL_DIR/"

# Criar o diretório Desktop se ele não existir
mkdir -p "$HOME/Desktop"

# Criar o arquivo .desktop
DESKTOP_FILE="$HOME/Desktop/GeradorDePecasDXF.desktop"
cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Version=1.0
Name=Gerador de Peças DXF
Comment=Gerador de Peças DXF
Exec=$INSTALL_DIR/maquina
Icon=$INSTALL_DIR/icon.png
Terminal=false
Type=Application
Categories=Utility;
EOF

# Tornar o arquivo .desktop executável
chmod +x "$DESKTOP_FILE"

# Mensagem de sucesso
echo "Instalação concluída com sucesso. Um ícone foi criado na área de trabalho."