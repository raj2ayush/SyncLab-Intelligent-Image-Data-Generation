import os
import glob
import cv2
import subprocess
import matplotlib.pyplot as plt

def validatee1():
    cmd = f"python emotions.py --mode display"
    subprocess.run(cmd, shell=True)