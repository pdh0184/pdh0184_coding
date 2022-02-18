import requests
res = requests.get("https://www.google.com/")
res.raise_for_status()#requests.get으로 가져온 코드가 정상인지 아닌지 판단 정상이 아니라면 다음 코드가 실행되지 않는다.
#print(len(res.text)) len은 문자갯수를 알려줌
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)