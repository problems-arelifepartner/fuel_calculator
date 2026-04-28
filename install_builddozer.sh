#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "========================================"
echo "   Buildozer Automated Installer"
echo "========================================"

echo -e "\n[1/4] Updating package lists and upgrading system..."
sudo apt update
sudo apt upgrade -y

echo -e "\n[2/4] Installing system dependencies (Java, Compilers, Git, etc.)..."
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

echo -e "\n[3/4] Installing Cython, Virtualenv, and Buildozer via pip..."
# Note: Cython is pinned to 0.29.33 for maximum Kivy compatibility
pip3 install --user --upgrade Cython==0.29.33 virtualenv buildozer

echo -e "\n[4/4] Configuring the PATH variable..."
# Check if .local/bin is already in .bashrc to avoid duplicate entries
if grep -q "~/.local/bin" ~/.bashrc; then
    echo "~/.local/bin is already in your ~/.bashrc"
else
    echo 'export PATH=$PATH:~/.local/bin/' >> ~/.bashrc
    echo "Successfully added ~/.local/bin to your ~/.bashrc"
fi

echo -e "\n========================================"
echo " Installation Complete!"
echo "========================================"
echo "IMPORTANT: To apply the PATH changes to your current terminal, run:"
echo "source ~/.bashrc"
echo "========================================"
