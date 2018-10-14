import sys
import os

print(f'Version: {sys.version}')
print(f'Installation: {sys.executable}')
print(f'Virtualenv: {os.getenv("VIRTUAL_ENV")}')