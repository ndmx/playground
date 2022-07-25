import pyautogui as gui
import time

# pause 5 seconds while you set focus to the terminal/console window:
print('Click on the terminal/console window where the automated keyboard data needs to be entered...')
print('NOTE: You have 5 seconds to do this!')
time.sleep(5)

# auto type test data from text file:
with open('alexa.txt', 'r') as tst:
    time.sleep(1)
    tst = tst.readlines()
    for i in range(0, len(tst), 1):
        print(tst[i])
        gui.typewrite(tst[i])
    gui.press('enter')
    gui.typewrite('Thank you Aviva!\n')
print('Auto data input completed.')

