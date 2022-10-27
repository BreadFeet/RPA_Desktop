# 파일 기본
import os
print(os.getcwd())     # current working directory

# os.chdir("7. RPA_desktop")   # RPA_desktop으로 작업 공간 변경
# print(os.getcwd()) 

# os.chdir("..")     # 상대경로 - 상위 폴더로 이동
# print(os.getcwd()) 
# os.chdir("../..")  # 두 단계 상위 폴더로 이동 
# print(os.getcwd()) 

# os.chdir("c:/")     # 주어진 절대 경로로 이동
# print(os.getcwd()) 

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)      # 절대경로: 현재작업공간/my_file.text 생성

# # 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\sori-\Desktop\PythonWorkSpace"))
# # 경로를 알면 이미 폴더 정보를 아는 건데 왜 필요하지?????

# 파일 정보 가져오기
import time
import datetime

# # 파일 생성 날짜
# ctime = os.path.getctime("run_btn.png")
# print(ctime)        # 기원부터의 시간이 초로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))    # string format으로 바꾸기

# # 파일 수정 날짜
# mtime = os.path.getmtime("run_btn.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y/%m/%d %H:%M:%S"))

# # 파일에 마지막 액세스한 날짜
# atime = os.path.getatime("run_btn.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

# # 파일 크기
# size = os.path.getsize("run_btn.png")
# print(size)    # in byte

# 파일 목록 가져오기
# print(os.listdir())     # working directory의 파일목록 출력
# print(os.listdir("7. RPA_desktop"))   # 현재 working dir 아래 주어진 폴더의 파일목록 출력
# print(os.listdir("fake folder"))   # 하위-하위 폴더는 찾지 못함
# print(os.listdir("../../Documents"))

# 지정한 폴더의 모든 하위 폴더/파일 포함
# folders = os.walk("7. RPA_desktop")
# print(folders)     # <generator object walk at 0x02C16418>

# for root, dirs, files in folders :    # folder 결과는 3개의 tuple로 구성
#     print(root, dirs, files)   # 상위폴더 해당값 -> 하위폴더 해당값 순으로 끝까지 나옴

# 현재 작업공간의 모든 하위 폴더/파일 포함
# fldr = os.walk(".")
# print(fldr)

# for root, dirs, files in fldr :
#     print(root, dirs, files)

# 폴더 안에서 특정 파일을 찾으려면?
# name = "Thailand.py"    # 찾으려는 파일명
# result = []
# for root, dirs, files in os.walk(".") :
#     if name in files :
#         result.append(os.path.join(root, name))
# print(result)


# 특정 패턴을 가진 파일을 찾으려면?
# *.xlsx, *.txt, 자동화*.png...
# import fnmatch    # file name match
# pattern = "img*.png"
# result = []
# for root, dirs, files in os.walk(".") :
#     for name in files :    
#         if fnmatch.fnmatch(name, pattern) :
#             result.append(os.path.join(root, name))
# print(result)


# 주어진 경로가 파일인지, 폴더인지?
# print(os.path.isdir("7. RPA_desktop"))     # 폴더인지?
# print(os.path.isfile("7. RPA_desktop"))    # 파일인지?

# print(os.path.isdir("file_btn.png"))
# print(os.path.isfile("file_btn.png"))

# print(os.path.isdir("7. RPA_desktop/7. window.py"))
# print(os.path.isfile("7. RPA_desktop/7. window.py"))


# # 지정한 경로에 해당하는 파일/폴더가 없다면?
# print(os.path.isdir("image.py"))    # false
# print(os.path.isfile("image.py"))   # false

# 주어진 경로가 존재하는지?
if os.path.exists("run_btn.png") :   # Boolean
    print("The file exists")
else : 
    print("Not found")


#  현재 경로에 파일 만들기
open("new_file.txt", "a").close()    # 빈 파일 생성

# 파일명 변경하기
os.rename("new_file.txt", "new_renamed.txt")    # new_file --> new_renamed로 변경

# 파일 삭제하기
os.remove("new_renamed.txt")


# 현재 경로에 폴더 만들기
# os.mkdir("new_folder")   
# 절대 경로에 폴더 만들기
os.mkdir("c:/users/sori-/Desktop/soi")

# 하위 폴더를 가지는 폴더 생성
os.makedirs("new_folders/a/b/c")

# 폴더명 변경하기 - 파일과 동일!
os.rename("new_folder", "new_renamed")

# 폴더 삭제하기 - 폴더 안이 비어있어야만 삭제 가능
os.rmdir("new_renamed")               # os.rmdir: 폴더 하나만 삭제
os.rmdir("new_folders/a/b/c")         # 마지막 폴더 하나만 삭제

os.removedirs("new_folders/a/b/c")               # 비어있는 폴더는 모두 삭제
os.removedirs("c:/users/sori-/desktop/soi/a/b")  # 비어있는 폴더는 모두 삭제

# 폴더 안이 있더라도 모두 삭제하기 - 주의!!
import shutil      # shell utilities
shutil.rmtree("new_folders")
shutil.rmtree("c:/users/sori-/desktop/soi")


# 한 개 파일 복사하기
# 파일을 폴더 안에 같은 이름으로 복사하기
shutil.copy("run_btn.png", "test_folder")    # 이동할 파일 경로, 대상'폴더' 경로

# 파일을 폴더 안에 새로운 이름으로 복사하기
shutil.copy("run_btn.png", "test_folder/run_btn_copy.png")   # 이동할 파일 경로, 이동된 '파일' 경로
shutil.copyfile("run_btn.png", "test_folder/run_btn_copy_2.png")  # 대상 폴더 경로 적으면 오류
shutil.copy2("run_btn.png", "test_folder/run_btn_copy2.png")   # syntax는 copy와 같음

# copy, copyfile: meta 정보 복사 X --> 현재 새로 만든 것처럼 저장됨
# copy2: meta 정보 복사 O --> 원본 정보 그대로 유지

# 폴더 안 전체 폴더/파일 복사하기
shutil.copytree("test_folder", "test_folder2")  # 원본 폴더 경로, 대상 폴더 경로(새로운 폴더)
shutil.copytree("test_folder", "6. RPA_Excel", dirs_exist_ok=True)    # 대상 폴더 경로(기존 폴더)
shutil.copytree("7. RPA_desktop", "test_folder3") # 하위 폴더/파일 모두 복사


# 이동하기(cut&paste) 
shutil.move("run_btn.png", "7. RPA_desktop")    # 파일 이동
shutil.move("test_folder2", "test_folder3")   # 새로운 폴더로 이동: 폴더 자체가 아니라 컨텐츠만 이동 --> 폴더명 변경 효과!!
shutil.move("test_folder3", "7. RPA_desktop")   # 기존 폴더로 이동: 폴더 자체가 이동
