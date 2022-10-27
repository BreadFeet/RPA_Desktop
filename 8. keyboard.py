import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]   # 메모장 가져옴
w.activate()
# w.minimize()
# w.restore()

# 타이핑 - 영문, 숫자만 가능 (한글 안됨)
pyautogui.write("12345")
# list일 때는 key이름 자체를 넣어줌. 타이핑 간격 0.3초
pyautogui.write(["capslock", "s", "o", "r", "i", "left", "left", "right", "r", "enter", "right", "backspace"], interval=0.3)
# key names: https://automatetheboringstuff.com/2e/chapter20/

# 특수 문자 (shift 누르고 hold)
# pyautogui.keyDown("shift")   # shift press & hold
# pyautogui.press("4")   # 4 press & release
# pyautogui.keyUp("shift")     # shift release

# 조합키 (hotkey)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")     # press("a")와 같음
# pyautogui.keyUp("ctrl")  # ctrl + a
# pyautogui.hotkey("ctrl", "a")   # ctrl 누르고 a 눌렀다가 a 떼고 ctrl 떼는 순서

# 한글 입력 - 클립보드에 저장한 뒤 붙여넣기
# pip install pyperclip 설치
import pyperclip    
# pyperclip.copy("쇼이는 미래꿈나무")     # 문장을 클립보드에 집어넣음
# pyautogui.hotkey("ctrl", "v")        # 붙여넣기

def kr_write(text) :
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

kr_write("쇼이는 데이터 사이언티스트")

# 자동화 프로그램 종료: ctrl + alt + diel