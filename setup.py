
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base, icon="Desktop_Icon.ico")]

includefiles = [
    "Desktop_Icon.ico",
    "tcl86t.dll",
    "tk86t.dll",
    "config.ini",
    "public",
    "data",
    "attendance_report",
    "classifier.xml",
    "haarcascade_frontalface_default.xml",
    "database"
]

options = {
    "build_exe": {
        "packages": ["tkinter"],
        "include_files": includefiles,
        "excludes": ["__pycache__"],  
    }
}


setup(
    name="Attendance marking using multiple face recognition Software",
    version="1.0",
    description="Attendance marking system using multiple face recognition system | Developed By Ganesh Kumar",
    options=options,
    executables=executables
)
