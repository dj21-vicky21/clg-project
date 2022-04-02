import os
from gtts import gTTS
from googletrans import Translator, constants
from playsound import playsound


def speak(text):
    translator = Translator()
    translation = translator.translate(text=text,dest='ta')
    text = translation.text
    print(text)
    tts = gTTS(text,lang='ta')
    tts.save('audio.mp3')
    playsound('audio.mp3')
    os.remove('audio.mp3')
speak('hello')