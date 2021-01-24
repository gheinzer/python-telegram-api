import toml
import time
import os

print("ImageRenameAgent 2021")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("Copyright by Gabriel Heinzer")
print()
print("CONFIGURATION WIZARD")

try:
    tomlfile = open("config.toml", "r")
    oldtoml = toml.load(tomlfile)
    try:
        if oldtoml["configurated"]:
            already_configurated = True
    except KeyError:
        already_configurated = False
    tomlfile.close()
except FileNotFoundError:
    already_configurated = False

print("Hallo!")
time.sleep(1)
print("Vielen Dank, dass Sie den ImageRenameAgent benutzen.")
time.sleep(1)
if already_configurated:
    print("Wir haben bemerkt, dass Sie den ImageRenameAgent bereits konfiguriert haben.\n")
    time.sleep(1)
    print("Um die Einstellungen zu ändern, bitte benutzen Sie 'py -m ira'.")
    time.sleep(1)
else:
    config = {"configurated": True}
    config["pathes"] = []
    cascadefiles = os.listdir("cascades")
    cascades = []
    for i in cascadefiles:
        objectname = i.replace(".xml", "")
        cascades.append(objectname)
    config["configurated_objects"] = list(cascades)

    tomlfile = open("config.toml", "w")
    toml.dump(config, tomlfile)
    tomlfile.close()
