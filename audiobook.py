import os
from tkinter.filedialog import askopenfilename
import pyttsx3
import PyPDF2
from gtts import gTTS
from googletrans import Translator, constants
from PIL import Image
import pytesseract
import cv2,sys
from playsound import playsound
import platform
import time
from fpdf import FPDF

#language function
def lang():
    dic = {'ta': 'tamil','en': 'english', 'te': 'telugu','hi': 'hindi','fr': 'french','es': 'spanish','af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch',  'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish',  'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew',  'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',  'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik',  'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
    count = 1
    words = []
    for key ,item in dic.items():
        words.append(item)
    for i in words:
        print("Enter No {} : {}".format(count,(i[0].upper()+i[1:])))
        count+=1
    lists = []
    for key,item in dic.items():
        lists.append(key)
    lists = [None]+lists
    checker = True
    while checker:
        num =int(input("\nEnter the option: "))
        if num <= len(dic):
            return lists[num]
            checker =False
        else:
            print('\nWrong Number Entered!')

# speak function

def speak(text,lang):
    translator = Translator()
    translation = translator.translate(text,dest=lang)
    text = translation.text
    print(text)
    tts = gTTS(text,lang=lang)
    tts.save('evoice-speaker.mp3')
    playsound('evoice-speaker.mp3')
    os.remove('evoice-speaker.mp3')

# save function

def save(text,lang):
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
            print('\nsucessfully saved')
        else:
            print('\nfile already exist!')

# main function


def audio():
	x = "#" * 30
	y = "=" * 28
	global bye 
	bye = "\n {}\n# {} #\n# ===><===  ===> Thank you for interseted in  your project <===  ## ===><=== #\n# {} #\n {}".format(x, y, y, x) 

	#Printing Welcome Message And options For This Program
	print(""" 

  ------------------------------------------------------
 |======================================================| 
 |========	 Welcome To Audiobook           ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To using pdf 
Enter 2 : To Using photo 
Enter 3 : To Using custiom text
Enter 4 : To using camera
		
		""")

	try: 
		userInput = int(input("\nPlease Select An Above Option: "))
	except ValueError:
		exit("\nHy! That's Not A Number") 
	else:
		print("\n")

	if(userInput<=4):
		LANG = lang()


# ............................................................. 

# pdf to speak 

	if (userInput == 1):
		pdf = askopenfilename()
		pdfReader = PyPDF2.PdfFileReader(pdf)
		pages=pdfReader.numPages
		for p in range(pages):
			page = pdfReader.getPage(p)
			text = page.extractText()
			cv2.destroyAllWindows()
			print('''
Enter 1: To lisen evoice
Enter 2: To save mp3
			''')
			if p > 0:
				speak('for next page',LANG)
			checker =True
			while checker:
				option1 = int(input('\nPlease Select An Above Option: '))
				if (option1 == 1):
					speak(text,LANG)
					checker = False
				elif(option1 ==2):
					save(text,LANG)
					checker = False
				else:
					print('\nError: Wrong Number Entered!')


# .............................................................

# img to speak

	elif (userInput == 2):
# get image
		image = Image.open(askopenfilename())
# get text from image
		text = pytesseract.image_to_string(image, lang="eng")
# translate
		translator = Translator()
		translation = translator.translate(text=text,dest=LANG)
		text = translation.text
		print('''
Enter 1: To lisen evoice
Enter 2: To save mp3
			''')
		checker = True
		while checker:
			option2 = int(input('\nPlease Select An Above Option: '))
			if (option2 == 1):
				speak(text,LANG)
				checker = False
			elif(option2 ==2):
				save(text,LANG)
				checker = False
			else:
				print('\nError: Wrong Number Entered!')
		cv2.destroyAllWindows()


# ..............................................................



# custom speak
	elif(userInput == 3):
		print('\n')
		text = str(input('\nEnter the text you want to speak: '))
		print('''
Enter 1: To lisen evoice
Enter 2: To save mp3
			''')
		checker = True
		while checker:
			option3 = int(input('\nPlease Select An Above Option: '))
			if (option3 == 1):
				speak(text,LANG)
				checker = False
			elif(option3 ==2):
				save(text,LANG)
				checker = False
			else:
				print('\nError: Wrong Number Entered!')


# .............................................................


	elif(userInput == 4):
# create dir
		cwd = os.getcwd()
		dir = "converter"
		parent_dir = cwd 
		path = os.path.join(parent_dir, dir) 
		
# initialization
		
		img_count =1
		dir_count = 1
		file_count = 0
		
# open camera
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
		

# get path of the file_dir
		file_dir = '{}/{}/'.format(cwd,dir)
		width ,height = 0,0
		cdir = "{}/".format(file_dir) 
		
# count the files 
		
		for pat in os.listdir(cdir):
			if os.path.isfile(os.path.join(cdir, pat)):
				file_count += 1
		print(file_count)
		time.sleep(20)
		i = 1
# loop using get text
		while i <= file_count:
			file_img = Image.open(file_dir +'img%.d.jpg' % i)
			text = pytesseract.image_to_string(file_img, lang="eng")
			# print(text.strip())
			text = text.strip()
			i +=1
			print('\n')
			if i > 2:
				speak('for next page',LANG)
			print('''
Enter 1: To lisen evoice
Enter 2: To save mp3
			''')
			checker =True
			while checker:
				option1 = int(input('\nPlease Select An Above Option: '))
				if (option1 == 1):
					speak(text,LANG)
					checker = False
				elif(option1 ==2):
					save(text,LANG)
					checker = False
				else:
					print('\nError: Wrong Number Entered!')

	# check greater than 4 are lesser than 1

	elif(userInput < 1 or userInput > 4): 
		print("\nPlease Enter Valid Option")
		time.sleep(2)
		audio()				

audio()

# repeat main function

def runAgain(): 
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): 
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		audio()
		runAgain()
	else:
		quit("\nbye")
runAgain()
		
