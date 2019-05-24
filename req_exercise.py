#환율을 알아보자

import requests
import bs4

res = requests.get('https://finance.naver.com/marketindex/').text
text = bs4.BeautifulSoup(res, 'html.parser')
usd = text.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')
print(usd.text)