from cx_Freeze import setup, Executable

files = ['assets','databaseProducts.db','pys6_msgBoxes','.env']

exe = Executable(script="app.py", base="win32GUI")

setup(
    name="Inventario",
    version="5.0",
    description="Inventario y contabilidad",
    author="Diego Martinez",
    author_email='diegomartinez1101@gmail.com',
    options={
        'build_exe': {
            'include_files': files,
            'excludes': ['msilib']
        }
    },
    executables=[exe],
    packages=['assets', 'databaseProducts.db', 'pys6_msgBoxes']
)

# python setup.py build_exe --zip-include-packages=encodings,PySide6 -----COMANDO PARA CREAR .EXE

# pyinstaller --onefile --add-data "assets;assets" --add-data ".env;." --add-data "pys6_msgBoxes;pys6_msgBoxes" app.py ----COMANDO PARA CREAR .EXE

