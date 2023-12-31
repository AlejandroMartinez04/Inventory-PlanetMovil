import sys
import os

from cx_Freeze import setup, Executable

files = ['assets','databaseProducts.db','pys6_msgBoxes','credentials.txt']

exe = Executable(script="app.py", base="win32GUI")

setup(
    name="Inventario PlanetMovil",
    version="4.0",
    description="Inventario y contabilidad para planet movil",
    author="Diego Martinez",
    author_email='diegomartinez1101@gmail.com',
    options={'build_exe': {'include_files': files}},
    executables=[exe]
)

# python setup.py build_exe --zip-include-packages=encodings,PySide6 -----COMANDO PARA CREAR .EXE

# python setup.py bdist_msi ---- CREA EL .EXE PARA INSTALACION DEL PROYECTO

# auto-py-to-exe

