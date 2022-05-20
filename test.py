from importlib.resources import path
from PIL import Image
import pytesseract
import cv2
import os

path = os.getcwd()
path_after = "/".join(path.split("\\"))
sum = 0.00

def threshold_By_OTSU(input_img_file):
    image=cv2.imread(input_img_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   ##要二值化图像，必须先将图像转为灰度图
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print("threshold value %s" % ret)  #打印阈值，超过阈值显示为白色，低于该阈值显示为黑色
    cv2.imwrite( path_after +'/temp_after.jpg', binary)


   
with Image.open(path_after +'/test.jpg') as im1:
    maxHeight = im1.size[1]
    box = (750, 418, 992, (maxHeight-227))
    im2 = im1.crop(box)
    im2.save(path_after +'/temp_middle.jpg')
threshold_By_OTSU(path_after +'/temp_middle.jpg')
with Image.open(path_after +'/temp_after.jpg') as im3:
    data2calculate = pytesseract.image_to_string(im3, config='-c tessedit_char_whitelist=0123456789. --psm 6')
    print(data2calculate)
data = data2calculate.split('\n')
for i in data:
    if i:
        if float(i)==200:
            pass
        else:
            sum = sum + float(i)
print(sum)

