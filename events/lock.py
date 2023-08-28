import os
import random
from ctypes import windll


def lock():
    chances = [False, False, True, True]
    if random.choice(chances):
        os.system("shutdown /p")
    else:
        windll.user32.LockWorkStation()
