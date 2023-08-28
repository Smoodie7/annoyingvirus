import ctypes
import random

errors = ("Win32.dll is probably corrupted.", "Windows System is unstable.", "\"msedge.exe\" just crashed.",
          "Impossible to get Microsoft UUID.", "None", "ValueError: Impossible to treat request.")


def error_popups():
    random.choices(errors)
    ctypes.windll.user32.MessageBoxW(0, random.choice(errors), u"An error has occurred", 0)
