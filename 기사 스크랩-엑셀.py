from typing import Sizedㄴ
import openpyxl
import urllib.request
from bs4 import BeautifulSoup
import re
import requests
excel = openpyxl.Workbook()
excel.create_sheet()
sheet = excel.active
sheet.column_dimensions['A'].width = 60
sheet.row_dimensions[1].height = 18
sheet.append(["기사제목","link"])

kward = input("검색어를 입력하세요:")
i = input("페이지 입력:")

page_num = 1
last_page = int(i)*10

while page_num < last_page:
    url =f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={kward}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page_num}"
    html = requests.get(url).text # url을 불러옴
    soup =BeautifulSoup(html, "html.parser")
    titles = soup.find_all("a" , {"class":"news_tit"} )

    for i in titles:
        print(i.attrs['title'])
        article = i.attrs['title']
        print(i.attrs["href"])
        link = i.attrs["href"]
        print()
        sheet.append([article,link])
        sheet.append([None,None])

    page_num += 10

excel.save(f"{kward} 기사.xlsx")