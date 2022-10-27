import pyautogui

pyautogui.sleep(3)   # 3초 대기
print(pyautogui.position())    # 3초 후 이동된 커서의 위치
# 전체 스크린을 2000*1000으로 생각하면 쉬움!

# 위에서 원하는 위치를 찾아두고 클릭하도록 함
pyautogui.click(594, 42, duration=1)   

# 클릭동작은 mouseDown과 mouseUp 동작을 합한 것
pyautogui.click()
pyautogui.mouseDown()   # 마우스 버튼 클릭
pyautogui.mouseUp()     # 마우스 버튼에서 손을 뗌

# 여러번 클릭
pyautogui.click(clicks=10)

# 드래그&드랍 1
# pyautogui.moveTo(100, 500, duration=0.3)   # 원하는 위치로 커서 이동
# pyautogui.mouseDown()       # 클릭 버튼 누름
# pyautogui.moveTo(250, 600, duration=0.3)   # 누른 채로 이동
# pyautogui.mouseUp()         # 드랍

# 드래스&드랍 2
# pyautogui.moveTo(474, 48)
# pyautogui.drag(250, 0, duration=0.3)    # 현재 위치 기준, 상대좌표로 이동
# pyautogui.dragTo(710, 48, duration=0.3)    # 절대 좌표로 이동

# 오른쪽 클릭
# pyautogui.rightClick()

# 마우스 휠 클릭
# pyautogui.middleClick()

# 스크롤
pyautogui.scroll(-300, x=500, y=500)   # 위 방향으로 300만큼 스크롤
pyautogui.scroll(-500)  # 아래 방향으로 스크롤

