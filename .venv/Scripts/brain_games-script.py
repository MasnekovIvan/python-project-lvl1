#!c:\users\ohtha\documents\programming\hexlet\project_1\.venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'masnekovivan-brain-games','console_scripts','brain_games'
__requires__ = 'masnekovivan-brain-games'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('masnekovivan-brain-games', 'console_scripts', 'brain_games')()
    )
