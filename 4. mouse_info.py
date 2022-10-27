import pyautogui

pyautogui.mouseInfo()  # 새 창에 마우스 정보 뜸
# 커서를 고정한 채로 필요한 값을 F키로 copy해서 사용

# 모든 동작에 1초씩 sleep 적용
pyautogui.PAUSE = 1 

# 자동화 작업을 중단하고 싶을 때(fail-safe) -> 커서를 네 귀퉁이에 가져가면 중단
for i in range(10) :   # 작업 10번 반복
    pyautogui.move(100, 100)    # 상대 좌표
    # pyautogui.sleep(1)


