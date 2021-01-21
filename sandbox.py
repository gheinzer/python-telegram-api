from haar_cascade import Detector
import os
myDetector = Detector(os.listdir("images"))
myDetector.detectAndFilter("faces")
