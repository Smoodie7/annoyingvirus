import ctypes


def rotate_screen(degrees):
    DMDO_DEFAULT = 0
    DMDO_90 = 1
    DMDO_180 = 2
    DMDO_270 = 3

    rotation_mapping = {
        0: DMDO_DEFAULT,
        90: DMDO_90,
        180: DMDO_180,
        270: DMDO_270
    }

    user32 = ctypes.windll.user32
    DM_DISPLAYORIENTATION = 0x00000080

    class DEVMODEW(ctypes.Structure):
        _fields_ = [
            ('dmDeviceName', ctypes.c_wchar * 32),
            ('dmSpecVersion', ctypes.c_short),
            ('dmDriverVersion', ctypes.c_short),
            ('dmSize', ctypes.c_short),
            ('dmDriverExtra', ctypes.c_short),
            ('dmFields', ctypes.c_int),
            ('dmOrientation', ctypes.c_short),
            ('dmPaperSize', ctypes.c_short),
            ('dmPaperLength', ctypes.c_short),
            ('dmPaperWidth', ctypes.c_short),
            ('dmScale', ctypes.c_short),
            ('dmCopies', ctypes.c_short),
            ('dmDefaultSource', ctypes.c_short),
            ('dmPrintQuality', ctypes.c_short),
            ('dmColor', ctypes.c_short),
            ('dmDuplex', ctypes.c_short),
            ('dmYResolution', ctypes.c_short),
            ('dmTTOption', ctypes.c_short),
            ('dmCollate', ctypes.c_short),
            ('dmFormName', ctypes.c_wchar * 32),
            ('dmLogPixels', ctypes.c_short),
            ('dmBitsPerPel', ctypes.c_int),
            ('dmPelsWidth', ctypes.c_int),
            ('dmPelsHeight', ctypes.c_int),
            ('dmDisplayFlags', ctypes.c_int),
            ('dmDisplayFrequency', ctypes.c_int),
            ('dmICMMethod', ctypes.c_int),
            ('dmICMIntent', ctypes.c_int),
            ('dmMediaType', ctypes.c_int),
            ('dmDitherType', ctypes.c_int),
            ('dmReserved1', ctypes.c_int),
            ('dmReserved2', ctypes.c_int),
            ('dmPanningWidth', ctypes.c_int),
            ('dmPanningHeight', ctypes.c_int),
            ('dmDisplayOrientation', ctypes.c_int),
            ('dmDisplayFixedOutput', ctypes.c_int)
        ]

    devmode = DEVMODEW()
    devmode.dmSize = ctypes.sizeof(DEVMODEW)
    devmode.dmFields = DM_DISPLAYORIENTATION
    devmode.dmDisplayOrientation = rotation_mapping[degrees]

    return user32.ChangeDisplaySettingsW(ctypes.byref(devmode), 0)

