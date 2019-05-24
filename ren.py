import os

#작업하고 있는 위치 변경
#os.chdir(r'')

#지정된 디렉토리로 전체 파일 목록 얻기
#os.listdir('폴더주소')

## 파일명 바꾸기(dummy 폴더에 있는 파일들의 이름을 한번에 바꾸자)

# 작업위치 변경
# 절대 주소를 사용하는 것이 좋다
os.chdir(r'C:\Users\student\PycharmProjects\190524\dummy')

# 폴더 안의 모든 파일을 불러와 이름을 변경하자
# f'지원자_{filename}' == 지원자_ + filename
#for filename in os.listdir('.'):
#    os.rename(filename, f'지원자_{filename}')

# replace로 변경
for filename in os.listdir('.'):
    os.rename(filename, filename.replace('지원자', '합격자'))
