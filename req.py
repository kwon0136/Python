# 새로운 라이브러리 설치
# Terminal창에서 pip install *라이브러리*

import requests
import bs4

# 주소에 요청을 보내서(requests) 정보를 받고(get) 텍스트 형태(text)로 변수 'res'에 저장
res = requests.get('https://finance.naver.com/sise/').text
#print(res)

# 주소의 상태 코드를 출력
#res = requests.get('https://www.naver.com').status_code
#print(res)


## 문서 전체에서 원하는 정보만 가져오자

#정보를 조작하기 편하게 변경
text = bs4.BeautifulSoup(res, 'html.parser')

#원하는 정보만 가져오자(.select / 원하는 하나의 정보: .select_one)
kospi = text.select_one('#KOSPI_now')
#print(kospi)

#알맹이만 뽑아오자(.text)
print(kospi.text)