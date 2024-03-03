from cx_Freeze import setup, Executable

files = ['assets','databaseProducts.db','pys6_msgBoxes']

exe = Executable(script="app.py", base="win32GUI")

setup(
    name="Inventario",
    version="4.6",
    description="Inventario y contabilidad",
    author="Diego Martinez",
    author_email='diegomartinez1101@gmail.com',
    options={'build_exe': {'include_files': files}},

    executables=[exe],
    packages=['assets','databaseProducts.db','pys6_msgBoxes']
)

# python setup.py build_exe --zip-include-packages=encodings,PySide6 -----COMANDO PARA CREAR .EXE

