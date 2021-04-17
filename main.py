import pyautogui, time

amountToSpam = 5
word = "beans"
time.sleep(10)
for _ in range(amountToSpam):
  pyautogui.typewrite(word)
  pyautogui.press("enter")
  time.sleep(1)
