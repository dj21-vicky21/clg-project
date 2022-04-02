import os
from gtts import gTTS
from googletrans import Translator, constants
from playsound import playsound

text = 'hello'
lang = 'ta'
# def save(text):
#     translator = Translator()
#     translation = translator.translate(text,dest=lang)
#     text = translation.text
#     tts = gTTS(text,lang=lang)
#     try:
#             filename = str(input('Enter the filename: '))
#             if (os.path.isfile(filename+'.mp3') == False):
#                 tts.save(filename+'.mp3')
#                 print('sucessfully saved')
#     except IOError:
#         print('file already exist')

# save(text)

def save(text):
    translator = Translator()
    translation = translator.translate(text,dest=lang)
    text = translation.text
    tts = gTTS(text,lang=lang)
    checker =True
    while checker:
        filename = str(input('Enter the filename: '))
        if (os.path.isfile(filename+'.mp3') == False):
            tts.save(filename+'.mp3')
            checker =False
            print('sucessfully saved')
        else:
            print('file already exist!')
    

save(text)