import pyautogui

pyautogui.displayMousePosition() #84 512



# @@@@@@@@@@@@@@@@@@
# import pyautogui  
# screenWidth, screenHeight = pyautogui.size() # returns the monitor size  
# print("The Screen Width is: ", screenWidth)  
# print("The Screen Height is: ", screenHeight)   

# currentMouseX, currentMouseY = pyautogui.position()  
# print("X Cordinate is: ", currentMouseX)  
# print("Y Cordinate is: ", currentMouseY)   

# print(pyautogui.onScreen(500, 600))   
# print(pyautogui.onScreen(0, 1500))    

# # pyautogui.rightClick(currentMouseX, currentMouseY)  

# pyautogui.scroll(100, 3831, 318)   

# pyautogui.KEYBOARD_KEYS  

# # pyautogui.typewrite('Sachin Kumar', 2)

# # pyautogui.alert(text='message box', title='MSG BOX', button='OK')  

# # pyautogui.confirm(text='Hello I am a message box', title='JavaTpoint', buttons=['OK', 'Cancel'])  


# pyautogui.password(text='Please Enter Your First Name', title='', default='', mask='*')  




# pyautogui.moveTo(100, 100, duration = 10)   

# --------------
# import pyautogui

# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# screenWidth, screenHeight
# (2560, 1440)

# currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
# currentMouseX, currentMouseY
# (1314, 345)

# pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

# pyautogui.click()          # Click the mouse.
# pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

# pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.doubleClick()     # Double click the mouse.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

# pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#         pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# # Shift key is released automatically.

# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

# pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.