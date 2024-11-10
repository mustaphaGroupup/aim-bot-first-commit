from PIL import ImageGrab

import math
import pyautogui
import cv2
import numpy as np
from pathlib import Path


def get_positions():
    rim = cv2.imread(str(Path("rim.png").absolute()))
    ball = cv2.imread(str(Path("ball.png").absolute()))
    screenshot = ImageGrab.grab(
        bbox=(0, 300, 1920, 1080),
        include_layered_windows=False,
        all_screens=False,
    )
    screenshot.save(
        "C:/Users/mchouria/Documents/Projects/ab/aim-bot-first-commit/screenshot.png"
    )
    templ = cv2.imread(str(Path("screenshot.png").absolute()))
    rim_position = cv2.matchTemplate(rim, templ, cv2.TM_CCOEFF_NORMED)
    ball_position = cv2.matchTemplate(ball, templ, cv2.TM_CCOEFF_NORMED)
    (rim_pos_y, rim_pos_x) = np.unravel_index(rim_position.argmax(), rim_position.shape)
    (ball_pos_y, ball_pos_x) = np.unravel_index(
        ball_position.argmax(), ball_position.shape
    )
    g = 981
    angle = 60
    delta_x = rim_pos_x - ball_pos_x
    delta_y = rim_pos_y - ball_pos_y - 2160

    v = math.sqrt(
        abs(
            (g * delta_x**2)
            / (2 * math.cos(angle) ** 2 * (delta_y + (delta_x * math.tan(angle))))
        )
    )
    print("ball: " + str(ball_pos_x) + " " + str(ball_pos_y))
    print("rim: " + str(rim_pos_x) + " " + str(rim_pos_y))
    print(v)


def move_mouse():
    pyautogui.dragTo(1800, 980, duration=0)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(1500, 580, duration=1)


get_positions()
move_mouse()
