import pyautogui

# 설치 확인
size = pyautogui.size()      # 현재 화면의 스크린 사이즈
print(size)
print(size[0])     # width 정보
print(size[1])     # height 정보

