import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui

image = cv2.imread("/home/must/Documents/Projects/aim bot/full.png")
template = cv2.imread("/home/must/Documents/Projects/aim bot/rim.png")
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
print(np.unravel_index(result.argmax(), result.shape))
