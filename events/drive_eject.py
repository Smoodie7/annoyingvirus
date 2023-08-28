import os
import ctypes


def find_cd_drive():
    for drive in range(ord('A'), ord('Z') + 1):
        drive_letter = f"{chr(drive)}:"
        if os.path.exists(drive_letter):
            try:
                volume_name = os.popen(f"vol {drive_letter}").read().strip().split('\n')[0]
                if "CD-ROM" in volume_name:
                    return drive_letter
            except Exception:
                continue
    return None


def eject_drive(drive_letter):
    ctypes.windll.winmm.mciSendStringW(f"set {drive_letter} door open", None, 0, None)


def close_drive(drive_letter):
    ctypes.windll.winmm.mciSendStringW(f"set {drive_letter} door closed", None, 0, None)
