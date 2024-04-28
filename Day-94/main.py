import pyautogui
import time
import keyboard

while True:
    im = pyautogui.screenshot()    
    screen = im.getpixel((84,512))
    
    x1 = im.getpixel((540,648))
    x2 = im.getpixel((251,630))
    x3 = im.getpixel((811,600))
    x4 = im.getpixel((956,631))
    
    y1 = im.getpixel((209,505))                    
    y3 = im.getpixel((739,531))
    y4 = im.getpixel((1027,512))
    
    if screen[0] == 255:
        if x1[0]!=255 or x2[0]!=255 or x3[0]!=255 or x4[0]!=255 or y1[0]!=255 or y2[0]!=255 or y3[0]!=255 or y4[0]!=255:
            pyautogui.press('space')
            time.sleep(0.0001)
    else:
        if x1[0]!=0 or x2[0]!=0 or x3[0]!=0 or x4[0]!=0 or y1[0]!=0 or y2[0]!=0 or y3[0]!=0 or y4[0]!=0:
            pyautogui.press('space')
            time.sleep(0.0001)    
            
    
    
    if keyboard.is_pressed('s'):
        break                         