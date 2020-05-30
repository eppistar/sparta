import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')


ranking = soup.find_all('td', {'class': 'number'})
titling = soup.find_all('a', {'class': 'albumtitle ellipsis'})
singers = soup.find_all('a', {'class': 'artist ellipsis'})

for i in range(0, len(ranking)):
    rank = i+1
    title = titling[i].text.strip()
    singer = singers[i].text.strip()
    print(rank,"위",title,singer)