import sys
sys.path.append("C:/Users/Gabriel Heinzer/OneDrive/Programme, Elektronik und Projekte/Python/telegram-bot-lib/module_file/")
from module_uninstaller import module_uninstaller

args = sys.argv


if len(args) > 1:
    if args[1] == "--help":
        helpdocsfile = open("helpdocs.txt", "r")
        helpdocs = helpdocsfile.read()
        helpdocsfile.close()
        print(helpdocs)
        

    if args[1] == "--uninstall":
        module_uninstaller.uninstall()

