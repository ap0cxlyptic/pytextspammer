from pynput.keyboard import Key,Controller
import time
Keyboard=Controller()
text=input("Enter the text to spam : ")
count=int(input("Number of spams : "))
time.sleep(10)
while(count>=1):
    for i in text:
        Keyboard.press(i)
        Keyboard.release(i)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    count=count-1