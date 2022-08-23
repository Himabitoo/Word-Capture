from PIL import Image
from tkinter import filedialog
import pyocr
import os

# C:\Users\kjun9\AppData\Local\Programs\Tesseract-OCR\\tesseract.exe
path = "C:\\Users\\User-name\\AppData\\Local\\Programs\\Tesseract-OCR"

os.environ['PATH'] = os.environ['PATH'] + path
typ = [('画像ファイル','*.png *.jpg')]
dir = 'D:\Mods\ImageWord\image'

print('使用する画像を選択してください。')
file = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
filename = os.path.basename(file)
print(f"You selected this file ---> {filename}")

pyocr.tesseract.TESSERACT_CMD = r'C:\Users\User-name\AppData\Local\Programs\Tesseract-OCR\\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

img = Image.open(file)

builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

print(text)