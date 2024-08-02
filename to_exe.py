# setup.py
from cx_Freeze import setup, Executable

setup(
    name="Launch",
    version="0.1",
    description="Launch the PyRPG made in PyRPG Maker.",
    executables=[Executable("main.py")]
)