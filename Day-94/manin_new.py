import pyautogui
import time
import keyboard
from PIL import ImageGrab, ImageOps

replay = (954,570)
dino = (5, 577, 140, 730)
delta = 230
delta2 = 80       


def imagegrab():
    bbox = (dino[0] + delta, dino[1], dino[2] + delta, dino[3] - delta2)
    img = ImageGrab.grab(bbox)
    graying = ImageOps.grayscale(image=img)
    # graying.save('Day-93/Dino.jpg')
    b = graying.getcolors()
    a = sum(map(sum,graying.getcolors()))
    
    return a
print(imagegrab())
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.001)
    pyautogui.keyUp('space')
    time.sleep(0.001)
    
def restart():
    pyautogui.click(replay)
    
def main():
    restart()
    while True:
        imagegrab()
        if imagegrab() != 10110:
            jump()

if __name__ == '__main__':
    main()