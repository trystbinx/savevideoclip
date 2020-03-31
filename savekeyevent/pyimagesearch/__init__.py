import pyautogui
import numpy as np
import cv2
import time

class pyimage():
    def imagesearch(image, precision=0.8):
        im = pyautogui.screenshot()
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val < precision:
            return [-1,-1]
        return max_loc

    def imagesearch_loop(image, timesample, precision=0.8):
        pos = imagesearch(image, precision)
        while pos[0] == -1:
            time.sleep(timesample)
            pos = imagesearch(image, precision)
        return pos

