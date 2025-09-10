import pyttsx3
import sounddevice as sd #used for setting the device on wich to play through
import soundfile as sf #used for creating the soundfile.wav and playing it through the selected device
import threading
import msvcrt

engine = pyttsx3.init()
engine.setProperty('rate', 180) #set voice speech speed
engine.setProperty('volume', 1) #set voice volume

audio_arquive = "TTS.wav" 

device1 = 7 #select VB-cable device here
device2 = 6 #select you speaker/headphone here(for audio playback)

def speak(text, device1, device2):
    engine.save_to_file(text, audio_arquive)
    engine.runAndWait()
    data, samplerate = sf.read(audio_arquive)

    t1 = threading.Thread(target=play_audio, args=(data, samplerate, device1))
    t2 = threading.Thread(target=play_audio, args=(data, samplerate, device2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def play_audio(data, samplerate, device_index):
    sd.play(data, samplerate, device=device_index, blocking=True, latency=0.1)

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
    print("\nSelected voice:", voices[voice_index].name, "\n")

if __name__ == '__main__':
    list_devices()
    device1 = int(msvcrt.getch())
    voices()

    while True:
        text = input("> ")
        if text.strip(" ,.") == "":
            continue
        t = threading.Thread(target=speak, args=(text, device1, device2))
        t.start()