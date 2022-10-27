import pyautogui

# # 파일 메뉴 클릭하기
file_menu = pyautogui.locateOnScreen("file_menu.png")
# 캡쳐 = Window + Shift + s
print(file_menu)    # 화면 위에서 찾은 그림의 정보 반환
pyautogui.click(file_menu)    # 그림의 정중앙을 클릭

# # terminal의 휴지통 찾기
trash_icon = pyautogui.locateOnScreen("trash_icon.png")
pyautogui.moveTo(trash_icon)

# 이미지를 발견하지 못한 경우
scr = pyautogui.locateOnScreen("screenshot.png")
print(scr)       # None 출력
# pyautogui는 이미지 기반이기 때문에 해상도만 바껴도 못 찾을 확률이 높음

# 똑같은 이미지가 여러개 있는 경우
for i in pyautogui.locateAllOnScreen("py_icon.png") :
    print(i)
    pyautogui.click(i)


# 속도 개선 - terminal의 휴지통 찾기
# 1. GrayScale - 흑백으로 전환하여 비교, 30% 속도 개선, 정확도 떨어질 수 있음
trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
pyautogui.moveTo(trash_icon)

# 2. 범위 지정 - 엄청 빨라짐
trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1666, 630, 243, 184))
pyautogui.moveTo(trash_icon)

# 3. 정확도 조정 - 완전 똑같진 않아도 일정수준 이상 같으면 같다고 인식하는 것
# pip install opencv-python 설치
run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.6)   # 60% 이상 같은 그림 찾음
pyautogui.moveTo(run_btn)


# 클릭 대상이 있는 창이 화면에 떠있지 않는 경우
file_btn = pyautogui.locateOnScreen("file_btn.png")
if file_btn :
    pyautogui.click(file_btn)
else : 
    print("발견 실패")   # 현재 창에 없으므로, 바로 발견 실패 출력

# 창을 띄울때까지 기다리다 작동하도록 하는 방법 - while
while file_btn is None :   # 찾는 순간 반복문 탈출 
    print("발견 실패")  
    file_btn = pyautogui.locateOnScreen("file_btn.png")
pyautogui.click(file_btn)

# 계속 기다리지 않고, 일정 시간만 기다리기 - timeout
import time
import sys

timeout = 10     # 10초 대기
start = time.time()   # 시작 시간-기원부터 현재까지 시간이 초로 얻어짐
file_btn = None

while file_btn is None :
    file_btn = pyautogui.locateOnScreen("file_btn.png")
    end = time.time()    # 찾을 때 시간
    if end - start > timeout :     # 10초를 초과하는 경우
        print("시간 종료")
        sys.exit()     # 프로그램 종료
pyautogui.click(file_btn)

# 함수로 만들기

def find_target(img_file, timeout=30) :  # 이미지 찾기 함수
    start = time.time()
    target = None
    while target is None :
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout :
            break
    return target   # 이미지를 찾았을 수도 못찾았을 수도 있음

def click(img_file, timeout=30) :   # 이미지 클릭 함수
    target = find_target(img_file, timeout)
    if target :
        pyautogui.click(target)
    else :
        print(f"[TIME OUT {timeout}s] Target({img_file}) not found. Program terminated") 
        sys.exit("프로그램 종료")    # 굳이 안써도 프로그램은 끝남

click("file_btn.png", 10)

