# written by @arpankarmakar and tested on @swapnilsamui
# TODO: Update the code using selenium module instead of the three below ones
import webbrowser
import time
import pyautogui


group_invite_link = input("Paste the group invite link: ")
message = input("Enter the message: ")
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
    pyautogui.typewrite(f"{message} {str(i)}\n")
