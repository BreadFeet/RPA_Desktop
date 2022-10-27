# 1. 그림판 실행(단축키: win + r, 입력값: mspaint) 및 최대화
import pyautogui

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
# pyautogui.mouseInfo()   # (226,947)
pyautogui.click(226, 947)
pyautogui.sleep(5)  # 그림판 창이 느리게 뜨기 때문에, 텀이 없으면 아래서 제목 없음 창에 잡히지 않음

win = pyautogui.getWindowsWithTitle("제목 없음")[0]    # 그림판 창
win.maximize()


# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무곳에나 글자 입력
txt = pyautogui.locateOnScreen("textbox_icon.png")
import sys
if txt :
    pyautogui.click(txt)
else :
    print("nothing found")
    sys.exit()

# 흰 영역 클릭
# pyautogui.click(200, 500)
paint = pyautogui.locateOnScreen("paint.png")
pyautogui.click(paint.left+500, paint.top+400)

import pyperclip
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

# 번외) 폰트 크기 바꾸기
pyautogui.hotkey("ctrl", "a", interval=1)
pyautogui.moveTo(paint.left+230, paint.top+160)
pyautogui.click()
pyautogui.press(["3", "2", "enter"])


# # 3. 5초 대기 후 그림판 종료 - 저장하지 않고 종료
pyautogui.sleep(5)
win.close()
# pyautogui.mouseInfo()    # (944,529)
pyautogui.press(["right", "enter"])
