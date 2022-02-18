import urllib.request
from bs4 import BeautifulSoup
import re
import requests
kward = input("검색어를 입력하세요:")
i = input("페이지 입력:")
page_num = 1
last_page = int(i)*10
while page_num < last_page:
    url =f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={kward}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page_num}"
    #html = urllib.request.urlopen(url).read() #url을 불러옴 
    html = requests.get(url).text # url을 불러옴
#html = html.content #requests.get(url)에 바로 beautifulsoup을 실행하면  "doc"형식으로 가져와 object of type 'Response' has no len() 에러가 발생한다
#이것은 뒤에 .text 또는 .content 를 붙여주면 해결된다
    soup =BeautifulSoup(html, "html.parser")
#title = soup.find_all(attrs={"class" : re.compile('^api\_txt\_lines total\_tit \_')}) attrs =("a":"b")는 a속성의 b가 포함된 속성값을 찾아준다 
# #mark = soup.find_all("mark")
    titles = soup.find_all("a" , {"class":"news_tit"} ) #a 태그 안에 있는 class = news_tit을 찾아준다

    for i in titles:
        print(i.attrs['title']) #.attrs["a"] 는 a 요소를 찾아준다 
        print(i.attrs["href"])
        print()

    page_num += 10