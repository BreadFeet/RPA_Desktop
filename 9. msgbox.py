import pyautogui

pyautogui.countdown(3)    # countdown
print("자동화 시작")

# 확인 버튼만 있는 팝업
pyautogui.alert("자동화가 실패하였습니다", "!경고!")

# 확인/취소 버튼이 있는 팝업
# result = pyautogui.confirm("계속 진행하겠습니까?", "확인")
# print(result)    # 확인: OK, 취소: Cancel

# 사용자 입력을 받는 팝업
# result = pyautogui.prompt("파일명을 무엇으로 할까요?", "입력")
# print(result)     # 취소: None

# 패스워드 입력 받는 팝업
result = pyautogui.password("암호를 입력하세요", "암호")
print(result)