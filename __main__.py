import sys

print("ImageRenameAgent 2021")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("Copyright by Gabriel Heinzer")
versionfile = open("VERSION", "r")
print("Version: " + str(versionfile.read()))
versionfile.close()

# METADATA
copyright: "Gabriel Heinzer"
Version: 2.2
Name: "ImageRenameAgent"
Version: "1.0beta"
Summary: "With the image renamer, you can upload images to a specified path. Then, this program is looking for objects, that are registered an is renaming the images with the object name."

args = sys.argv
if(len(args) == 1):
    print()
    print("""Was möchten Sie machen?
    - Einen überwachten Pfad hinzufügen (newpath <path>)
    - Einen überwachten Pfad nicht mehr überachen lassen (deletepath <path>)
    - Die Hilfe öffnen (help)
    - Den ImageRenameAgent stoppen (stopagent)
    Sie können alle diese Kommandos als Parameter verwenden (Beispiel: 'py -m ira newpath')""")

if(len(args) == 2):
    print()
    print("Adding path to configuration file...")
