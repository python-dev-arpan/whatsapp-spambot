# written by @arpan and tested on @swap
import webbrowser
import time
import pyautogui


phone = "9735556785"
msg = input("Enter your msg: ")
times = int(input("How many times? "))
whatsapp_link = f"https://web.whatsapp.com/send?phone={phone}&app_absent=0"
webbrowser.open(whatsapp_link)
time.sleep(15)

for i in range(1, times + 1):
    pyautogui.typewrite(f"{msg} {str(i)}\n")
