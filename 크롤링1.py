import urllib.request
from bs4 import BeautifulSoup
import re
import requests
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
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