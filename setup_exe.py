#PyQtLog.py
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        }
 
setup(
      name = 'SkyshanTool',
      version = '1.0',
      windows = [{  
	        'script': 'StartTool.py',
	        'icon_resources': [(1, 'StartTool.ico')]
        }],
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )