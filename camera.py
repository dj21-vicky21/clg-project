import cv2,sys
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

# cv2.namedWindow('camera')
img_count =1

while True:
    _,frame = camera.read()
    cv2.imshow('test',frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print('Escape hit,close')
        break
    elif k%256 == 32:
        img_name = "img{}.png".format(img_count)
        cv2.imwrite(img_name,frame)
        print('screenshot taken')
        img_count+=1


camera.release()
cv2.destroyAllWindows()



# def tesseract():
#     path_to_tesseract=r''
#     Imagepath = ''
#     pytesseract.tesseract_cmd = path_to_tesseract
#     text = pytesseract.image_to_string(Image.open(Imagepath))
#     print(text[:-1])
# tesseract()

# import cv2

# camera = cv2.VideoCapture(0)

# cv2.namedWindow('camera')
# img_count =1

# while  True:
#     ret,frame = camera.read()
#     if not ret:
#         print('failed to grab frame')
#         break
#     cv2.imshow('test',frame)
#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         print('Escape hit,close')
#         break
#     elif k%256 == 32:
#         img_name = 'img{}'.format(img_count)
#         cv2.imwrite(img_name,frame)
#         print('screenshot taken')
#         img_count+=1

# camera.release()
# camera.destroyAllWindows()