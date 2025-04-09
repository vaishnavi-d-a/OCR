import cv2
import pytesseract
from PIL import Image

# Set the path to Tesseract-OCR
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("ocrtext.png") #load the image

gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)   #convert to grayscale to improve ocr accuracy

gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]   #apply threshold for better text extraction

text = pytesseract.image_to_string(gray)   #perform OCR to extract text

with open("out.txt" , "w" , encoding="utf-8") as file:   #save text to editable file
    file.write(text)

print("text extracted succesfully to out.txt")


