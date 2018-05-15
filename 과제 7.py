engkor_dict={}
while True:
    eng=str(input("영어 단어 : "))
    if (eng not in engkor_dict)and(eng!=""):
        print("사전이 비어 있습니다.")
        print("단어를 추가합니다.")
        kor=str(input("한글 단어 : "))
        engkor_dict[eng]=kor
        continue
    elif eng in engkor_dict:
        print(eng,":",engkor_dict[eng])
    elif eng=="":
        print(engkor_dict)
        break
