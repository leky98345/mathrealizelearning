import subprocess
import sys

required_modules = ['pycaw', 'pyqt5']

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
