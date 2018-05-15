a=str(input("문자열 : "))
k=""
for i in range (0, len(a)):
    if i != a[len(a)-1]:
        k=k+a[i]
        continue
    else:
        break
print("개별 문자 출력 : ", k)

j=""
for l in range (len(a)-1, -1, -1):
    if i != a[len(a)-1]:
        j=j+a[l]
        continue
    else:
        break
print("역순 개별 문자 출력 : ", j)
