from cgitb import text
from genericpath import isfile
import cv2
from PIL import Image
import sys
import os
import numpy as np

def main(target_dir, desired):
    contents = os.listdir(target_dir)
    imgs = []
    for file in contents:
        if file.endswith(".png"):
            imgs.append(file)

    for image in imgs:
        img = cv2.imread(os.path.join(target_dir, image))
        avg = np.average(img)
        if (desired and avg < 55) or (not desired and avg > 150):
            Image.fromarray(np.invert(img)).save(os.path.join(target_dir, image))
            print(f"Converted {image} ")


if __name__ == "__main__":
    target_dir = ""
    main(target_dir, int(sys.argv[1])) # the first arguement is either 0 for make the images dark theme or 1 for make them light theme
