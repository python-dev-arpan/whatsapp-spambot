# written by @arpan and tested on @swap
import webbrowser
import time
import pyautogui

# sending to an individual

""" phone = "9735556785"
msg = input("Enter your msg: ")
times = int(input("How many times? "))
webbrowser.open(f"https://web.whatsapp.com/send?phone={phone}&app_absent=0")
time.sleep(15)  # wait 15 secs for whatsapp web to load

for i in range(1, times+1):  # send messages on loop
    pyautogui.typewrite(f"{msg} {str(i)}\n")

if not "database.txt":
    file = open("database.txt", "w")
    with open("database.txt", "a") as file:
        file.write(f"{time.asctime()} - {phone} - '{msg}' x {times}\n")

else:
    with open("database.txt", "a") as file:
        file.write(f"{time.asctime()} - {phone} - '{msg}' x {times}\n") """


# sending to a group

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

if not "database.txt":
    file = open("database.txt", "w")
    with open("database.txt", "a") as file:
        file.write(f"{time.asctime()} - {group_invite_link} - '{msg}' x {times}\n")

else:
    with open("database.txt", "a") as file:
        file.write(f"{time.asctime()} - {group_invite_link} - '{msg}' x {times}\n")
