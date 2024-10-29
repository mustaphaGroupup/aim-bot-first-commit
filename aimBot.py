from PIL import ImageGrab

# import pyautogui
import cv2
import numpy as np


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def get_positions():
    rim = cv2.imread("/home/must/Documents/Projects/aim bot/ball.png")
    ball = cv2.imread("/home/must/Documents/Projects/aim bot/rim.png")
    screenshot = ImageGrab.grab(
        bbox=(0, 1300, 1920, 2160),
        include_layered_windows=False,
        all_screens=False,
    )
    screenshot.save("/home/must/Documents/Projects/aim bot/screenshot.png")
    templ = cv2.imread("/home/must/Documents/Projects/aim bot/screenshot.png")
    rim_position = cv2.matchTemplate(rim, templ, cv2.TM_CCOEFF_NORMED)
    ball_position = cv2.matchTemplate(ball, templ, cv2.TM_CCOEFF_NORMED)
    print(np.unravel_index(rim_position.argmax(), rim_position.shape))
    print(np.unravel_index(ball_position.argmax(), ball_position.shape))


# def get_rim_approx_pos(image, size):
#     for x in range(135, 146):
#         for y in range(424, 446):
#             if all(x != y for x, y in zip(image.getpixel((x, y)), (255, 255, 255))):
#                 # if image.getpixel((x, y)) == (36, 39, 58):
#                 # print("#%02x%02x%02x" % image.getpixel((x, y)))
#                 print(
#                     rgb_to_hex(
#                         image.getpixel((x, y))[0],
#                         image.getpixel((x, y))[1],
#                         image.getpixel((x, y))[2],
#                     )
#                 )


# def move_mouse():
#     pyautogui.dragTo(1800, 980, duration=0)
#     pyautogui.mouseDown(button="left")
#     pyautogui.dragTo(1500, 480, duration=1)


# # Capture the entire screen
# screenshot = ImageGrab.grab()

# # Save the screenshot to a file
# screenshot.save("./screenshot.png")

# get_rim_approx_pos(screenshot, screenshot.size)
get_positions()
