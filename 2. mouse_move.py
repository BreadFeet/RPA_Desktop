import pyautogui

# "절대" 좌표로 마우스 이동
# 화면 왼쪽 위 꼭지점: x=0, y=0
pyautogui.moveTo(500, 300)    # 실행하면 지정한 위치로 마우스를 이동
pyautogui.moveTo(1000, 400, duration=5)   # 움직이는 속도 조절

# 연속 동작
# pyautogui.moveTo(100, 100, duration=0.3)
# pyautogui.moveTo(200, 200, duration=0.3)
# pyautogui.moveTo(300, 300, duration=0.3)

# "상대" 좌표로 마우스 이동 (현재 커서 기준)
# pyautogui.moveTo(100, 100, duration=0.3)
# print(pyautogui.position())    # Point(x, y) 위치 출력됨
# pyautogui.move(100, 100, duration=0.3) # 절대좌표 (200, 200) 으로 이동
# print(pyautogui.position())    
# pyautogui.move(100, 100, duration=0.3) # 결국 위와 같은 결과
# print(pyautogui.position())   

p = pyautogui.position()
print(p[0])    # x 좌표값
print(p[1])    # y 좌표값
print(p.x, p.y)   