import pyautogui
import time


# make variable anadir1 with a coords
anadir1 = (1554, 649)
anadir2 = (1570, 765)
anadir3 = (1556, 875)
anadir4 = (1552, 990)
anadir5 = (1556, 1095)
anadir6 = (1558, 1213)
anadir7 = (1577, 1330)
anadir8 = (1556, 1440)
anadir9 = (1569, 1420)



volver1 = (884, 1481)
volver2 = (1626, 357)


def anadir():
    pyautogui.click(anadir1)
    time.sleep(0.05)
    pyautogui.click(anadir2)
    time.sleep(0.05)
    pyautogui.click(anadir3)
    time.sleep(0.05)
    pyautogui.click(anadir4)
    time.sleep(0.05)
    pyautogui.click(anadir5)
    time.sleep(0.05)
    pyautogui.click(anadir6)
    time.sleep(0.05)
    pyautogui.click(anadir7)
    time.sleep(0.05)
    pyautogui.click(anadir8)
    time.sleep(0.05)
    pyautogui.click(anadir9)
    time.sleep(0.05)



def volver():
    pyautogui.click(volver1)
    time.sleep(0.1)
    pyautogui.click(volver2)
    time.sleep(8)


while True:
    anadir()
    volver()