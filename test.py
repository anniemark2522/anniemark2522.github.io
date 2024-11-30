subject=['datacom','os','comarch']
for subname in subject:
    sumscore=0
    print(subname)
    for i in range(1,4,1):
        score=int(input("Enter your score :"))
        sumscore=sumscore+score
    print(sumscore)