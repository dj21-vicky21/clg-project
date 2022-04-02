from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract
import os
from gtts import gTTS
from googletrans import Translator, constants
from playsound import playsound
import cv2


image = Image.open(askopenfilename())
text = pytesseract.image_to_string(image, lang="eng")
cv2.destroyAllWindows()



# translator = Translator()
# translation = translator.translate(text=text,dest='ta')
# text = translation.text

print(text.strip())

# tts = gTTS(text,lang ='ta')

# tts.save('audio.mp3')
# # playsound('audio.mp3')
# # os.remove('audio.mp3')




