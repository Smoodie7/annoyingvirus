import ctypes
import os

def set_wallpaper(path):
    # Function to set the wallpaper on Windows
    # It uses the SystemParametersInfo function from user32.dll
    # Requires the full path of the image file
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, SPIF_UPDATEINIFILE)

def save_wallpaper():
    # Function to save the current wallpaper
    # It retrieves the current wallpaper file path from the registry
    # and copies the file to a specified location
    import shutil
    import winreg

    # Get the current wallpaper file path from the registry
    key_path = r"Control Panel\Desktop"
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)
    wallpaper_path = winreg.QueryValueEx(reg_key, "Wallpaper")[0]

    # Copy the wallpaper file to a specified location
    saved_wallpaper_path = os.path.join(os.getcwd(), "saved_wallpaper.jpg")
    shutil.copy(wallpaper_path, saved_wallpaper_path)

    return saved_wallpaper_path

def restore_wallpaper(path):
    # Function to restore the saved wallpaper
    set_wallpaper(path)
    os.remove(path)

