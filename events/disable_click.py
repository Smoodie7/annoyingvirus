from ctypes import windll


def disable_mouse(value):
    windll.user32.BlockInput(value)
