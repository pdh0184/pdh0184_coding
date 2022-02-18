r= open(r"C:\Users\pdh01\OneDrive\바탕 화면\VSC\스마트 스토어 키워드\스마트스토어키워드.txt", "r")
a = r.read().split()
a_str = " ".join(r.read())
print(a)
new_kward = ["","심장영양제","관절사료"]
new_kwards = []

for kward in new_kward:
    if kward not in a:
        new_kwards.append(kward)

new_kwards_str = " ".join(new_kwards)
c= a_str + new_kwards_str
fw =open(r"C:\Users\pdh01\OneDrive\바탕 화면\VSC\스마트 스토어 키워드\스마트스토어키워드.txt", "a")
fw.write(new_kwards_str)
fw.close()
