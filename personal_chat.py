# written by @arpankarmakar and tested on @swapnilsamui
# TODO: Update the code using selenium module instead of the three below ones
import webbrowser
import time
import pyautogui


phone = input("Enter the phone no: ")
message = input("Enter the message: ")
times = int(input("How many times? "))
whatsapp_link = f"https://web.whatsapp.com/send?phone={phone}&app_absent=0"
webbrowser.open(whatsapp_link)
time.sleep(15)

for i in range(1, times + 1):
    pyautogui.typewrite(f"{message} {str(i)}\n")
