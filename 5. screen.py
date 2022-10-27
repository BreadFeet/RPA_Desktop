import pyautogui

# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# RGB 값 확인
# pyautogui.mouseInfo()   # 1103,64 81,154,186 #519ABA

# 해당 좌표의 pixel RGB 값을 확인
pixel_RGB = pyautogui.pixel(1103, 64)
print(pixel_RGB)          # (81, 154, 186)로 동일

# 내가 알고 있는 pixel RGB가 진짜 좌표의 RGB가 맞는지 확인하는 법
match = pyautogui.pixelMatchesColor(1103,64, (81, 154, 187))    # boolean
# match = pyautogui.pixelMatchesColor(1103,60, pixel_RGB) 
print(match)