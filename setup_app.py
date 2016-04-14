"""
Usage:
    python setup.py
"""

import os
import platform

plat = platform.system()

if plat == "Darwin": #mac
	# print plat
	setup = 'pyinstaller -w  --onefile --icon="StartTool.icns" StartTool.py'
	os.system(setup)
elif plat == "Windows":
	setup = 'pyinstaller -w  --onefile --icon="StartTool.ico" StartTool.py'
	os.system(setup)
