# written by @arpan and tested on @swap
import webbrowser
import time
import pyautogui


group_invite_link = "https://chat.whatsapp.com/IilqfeonwkD9NoTzluspl4"
msg = input("Enter your msg: ")
times = int(input("How many times? "))
webbrowser.open(group_invite_link)
time.sleep(15)
pyautogui.click(668, 551, clicks=2)
time.sleep(15)
pyautogui.click(670, 424, clicks=2)
time.sleep(15)
pyautogui.click(732, 699, clicks=2)
time.sleep(15)
for i in range(1, times + 1):
    pyautogui.typewrite(f"{msg} {str(i)}\n")
