import sys
from tqdm import tqdm as pb
import toml
from 


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
    Sie können alle diese Kommandos als Parameter verwenden (Beispiel: 'py -m ira newpath "Z:/Multimedia/')""")

if len(args) == 3 and args[1] == "newpath":
    newpath = args[2]
    print()
    progbar = pb(total=3)
    progbar.set_description("Opening TOML")
    tomlfile = open("config.toml", "r")
    progbar.set_description("Reading TOML")
    oldtoml = toml.load(tomlfile)
    tomlfile.close()

    if(newpath in oldtoml["pathes"]):
        progbar.close()
        print("Wir haben bewerkt, dass dieser Pfad schon überwacht wird.")
    else:
        progbar.set_description("Updating TOML")
        oldtoml["pathes"].append(newpath)
        tomlfile = open("config.toml", "w")
        toml.dump(oldtoml, tomlfile)
        progbar.set_description("Finished")
        progbar.close()
        tomlfile.close()