import pytesseract
import requests
import cv2
import numpy as np


def process_pic(img_url):
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

  response = requests.get(img_url)
  img_array = np.array(bytearray(response.content), dtype=np.uint8)
  img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

  # preprocess image
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  contrast_enhanced = clahe.apply(gray)
  _, binary = cv2.threshold(contrast_enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  denoised = cv2.medianBlur(binary, 3)
  
  kernel = np.ones((1,1), np.uint8)
  dilated = cv2.dilate(denoised, kernel, iterations=1)
  processed_image = cv2.erode(dilated, kernel, iterations=1)
  text = pytesseract.image_to_string(processed_image).split('/n')

  result = {
    'floors': '',
    'loss': '',
    'turns': '',
    'bonus': ''
  }

  text_to_find = [
    ['floors', 'Completed x', 'terminés x'],
    ['loss', 'Lost x', 'perdus x'],
    ['turns', 'Taken x', 'joués x'],
    ['bonus', 'Earned x', 'gagnés x']
  ]

  for line in text:
    print(line)
    for to_find in text_to_find:
        for i in range(1,3):
          if (to_find[i] in line):
            to_write = line.split(to_find[i])[1]
            if ' ' in to_write:
                to_write = to_write.split(' ')[0]
            if '\n' in to_write:
                to_write = to_write.split('\n')[0]
            result[to_find[0]] = int(to_write)
        
  result['score'] = result['floors'] * 50000 - result['loss'] * 1000 - result['turns'] * 100 + result['bonus'] * 250

  return result