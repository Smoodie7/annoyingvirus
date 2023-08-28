import pyaudio
import wave
import ctypes

def play_audio(index):
    # Define audio settings
    chunk = 1024

    # Provide the full path to the file
    file_path = f'C:\\Program Files\\Startup Data\\audio{index}.wav'

    wf = wave.open(file_path, 'rb')

    # Create a PyAudio instance
    p = pyaudio.PyAudio()

    # Open a streaming object
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    while data := wf.readframes(chunk):
        stream.write(data)
    # Cleanup
    stream.stop_stream()
    stream.close()
    p.terminate()


def set_volume(volume):
    # Constants
    SNDVOL32_DLL = 'SndVol32.dll'
    HWND_BROADCAST = 0xFFFF
    WM_APPCOMMAND = 0x319
    APPCOMMAND_VOLUME_UP = 0x0A

    # Load the DLL
    winmm = ctypes.WinDLL(SNDVOL32_DLL)

    # Calculate the number of volume steps based on the desired volume percentage
    max_volume = 65535  # Maximum volume level
    volume_steps = int((volume / 100) * max_volume)

    # Send the volume command with the calculated volume steps
    winmm.SendMessageW(HWND_BROADCAST, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_UP | volume_steps)
