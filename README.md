the scrip requires VBcable, python(im using py312), pyttsx3, sounddevice and soundfile

to install the dependencies you can run in the cmd: py -m pip install pyttsx3 soundfile sounddevice
if the comand doesnt work, then try asking chatgpt or putting the error in a search engine

im leaving a .venv for VScode with the dependencies installed
just leave it in the same folder as the .py and open the .py folder in VScode, it should detect the virtual enviroment

this program was made using wishtag's STTS(https://github.com/wishtag/speech-to-text-to-speech) + chatgpt

it works by:
1. listing the audio devices using sounddevice
2. prompting you to select wich audio device to play trough
3. listing the installed SAPI5 voice modules(you can get more by installing a new laguage in windows)
4. prompting you to select wich voice to use
5. reading your input
6. passing your input to pyttsx3 for it to generate a "TTS.ogg/mp3/wav"
7. playing "TTS.ogg" trough the selected audio device using soundfile

you can set the speech rate/velocity and volume in "engine.setProperty('rate', 150)" and "engine.setProperty('volume', 1)"
you can set the TTS.ogg file format in "arquivo_audio = "TTS.ogg""
