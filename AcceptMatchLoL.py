import pyautogui
import time

accepted = False;

while not accepted:
    res = pyautogui.locateOnScreen("LoLAcceptButton.png", confidence=0.9)
    if res is not None:
        print("Found at:")
        print(res)
        acceptButton = pyautogui.center(res)
        pyautogui.moveTo(acceptButton)
        pyautogui.click()
        accepted = True
    else:
        print("Button not found, retrying...")
        time.sleep(1)