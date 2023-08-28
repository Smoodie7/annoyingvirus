import ctypes


def minimize_active_window():
    user32 = ctypes.windll.user32

    # Get the actual window
    hwnd = user32.GetForegroundWindow()

    # Minimize it
    user32.ShowWindow(hwnd, 6)
