import os
import time

packages = ["toml", "icrawler", "opencv-python", "tqdm", "tinydb", "markdown"]


for i in packages:
    print("installing " + i)
    process = os.system("sudo python -m pip install " + i)
    print()
    print()
    print()
    print()
