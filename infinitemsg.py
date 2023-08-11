import pyautogui as auto
import time 
i=0
while i<=12:
    auto.write("hello")
    
    auto.press("enter")
    time.sleep(0.2)
    i+=1  

    