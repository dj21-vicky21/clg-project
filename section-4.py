import os
from tkinter.filedialog import askopenfilename
import pyttsx3
import PyPDF2
from pdf2image import convert_from_path
from gtts import gTTS
from googletrans import Translator, constants
from PIL import Image
import pytesseract
import cv2,sys
from playsound import playsound
import platform
import time
from fpdf import FPDF
import shutil

# creating dir

cwd = os.getcwd()
dir = "converter"
parent_dir = cwd 
path = os.path.join(parent_dir, dir) 

# initialization

img_count =1
dir_count = 1
file_count = 0


# camera open

camera = cv2.VideoCapture(0)
while True:
    _,frame = camera.read()
    cv2.imshow('test',frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print('Escape hit,close')
        break
    elif k%256 == 32:
        if dir_count == 1:
            os.mkdir(path)
            dir_count+=1
        img_name = "{}/{}/img{}.jpg".format(cwd,dir,img_count)
        cv2.imwrite(img_name,frame)
        print('screenshot taken')
        img_count+=1
camera.release()
cv2.destroyAllWindows()


# file_count and dir_path
file_dir = '{}/{}/'.format(cwd,dir)

width ,height = 0,0
cdir = "{}/".format(file_dir) 

for pat in os.listdir(cdir):
    if os.path.isfile(os.path.join(cdir, pat)):
        file_count += 1
print(file_count)

# camera close
time.sleep(10)
i = 1
while i <= file_count:
    file_img = Image.open(file_dir +'img%.d.jpg' % i)
    text = pytesseract.image_to_string(file_img, lang="eng")
    print(text.strip())
    i +=1
    print('\n')
