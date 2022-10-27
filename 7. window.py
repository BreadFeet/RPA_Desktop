import pyautogui

fw = pyautogui.getActiveWindow()      # 현재 활성화된 창(vscode)
print(fw.title)    # vscode 창 제목을 가져옴
print(fw.size)     # 창의 크기 정보(width, height)
print(fw.left, fw.right, fw.top, fw.bottom)   
pyautogui.click(fw.left+10, fw.top+20)    # 창 기준 위치를 정해서 클릭

# 열려있는 모든 윈도우 창을 가져오기
for w in pyautogui.getAllWindows() :
    print(w)

# 단어를 포함하는 창 모두 가져오기
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False :     # 현재 활성화 되지 않았다면,
    w.activate()             # 화면 활성화 - 작동안함???

# if w.isMaximized == False :   # 최대화가 되지 않았다면,
#     w.maximize()              # 최대화 

# if w.isMinimized == False :   # 최소화 되지 않았다면,
#     w.minimize()              # 최소화 

pyautogui.sleep(1)
w.restore()         # 화면크기 복원

w.close()       # 윈도우 닫기 
# 저장할게 없으면 바로 닫히고, 있으면 팝업 뜬다.