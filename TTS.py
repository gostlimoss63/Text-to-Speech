import pyttsx3
import sounddevice as sd
import soundfile as sf
import threading
import msvcrt

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(texto, device_index):
    arquivo_audio = "TTS.ogg"

    engine.save_to_file(texto, arquivo_audio)
    engine.runAndWait()

    data, samplerate = sf.read(arquivo_audio)
    sd.play(data, samplerate, device=device_index)
    sd.wait()

def list_devices():
    print("Audio Output Device list")
    devices = sd.query_devices()
    for i, d in enumerate(devices):
        if d['max_output_channels'] > 0:
            print(f"{i}: {d['name']}")

def voices():
    print("Voice list")
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name}")
    voice_index = int(msvcrt.getch())
    engine.setProperty('voice', voices[voice_index].id)
    print ("\nSelected voice",voice_index,f"{voices[voice_index].name}","\n")

if __name__ == '__main__':
    list_devices()
    device_index = int(msvcrt.getch())
    print ("\nSelected device",device_index,"\n")
    voices()

    while True:
        texto = input("> ")
        if texto.strip(' ,.') == "":
            continue
        t = threading.Thread(target=speak, args=(texto, device_index))
        t.start()