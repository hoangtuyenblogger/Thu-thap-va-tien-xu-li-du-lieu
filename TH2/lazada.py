import pyautogui, pyperclip
from time import sleep
import random
print("TOOL SPAM TIN NHẮN FACEBOOK | HOANGTUYEN")


mess = input("Nhập tin nhắn cần spam: (Tin nhắn 1 | tin nhắn 2 | tin nhắn 3) : ").split("|")
n = int(input("Nhập số lần spam:"))

print("Chuẩn bị spam . . .")
for i in range(10, 0, -1):
    print(i, end="...", flush=True)
print("Bắt đầu spam . . . ")

for i in range(n):
    #pyperclip.copy(random.choice(mess))
    pyperclip.copy(mess[i])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    sleep(0.5)

print("Đã spam xong . . . . ")

