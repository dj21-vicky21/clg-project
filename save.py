import os
from gtts import gTTS
from googletrans import Translator, constants
from playsound import playsound

text = 'hello'
lang = 'ta'
def save(text):
    translator = Translator()
    translation = translator.translate(text,dest=lang)
    text = translation.text
    tts = gTTS(text,lang=lang)
    filename = str(input('Enter the filename: '))
    tts.save(filename+'.mp3')
    print('sucessfully saved')

save(text)