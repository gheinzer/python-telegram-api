import subprocess
import time

packages = ["toml", "icrawler", "opencv-python", "tqdm", "tinydb", "markdown"]


for i in packages:
    print("installing " + i)
    process = subprocess.call("py -m pip install " + i)
    print()
    print()
    print()
    print()
