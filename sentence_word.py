countlist = [1 for _ in range(11172)]
wordlist = {}
with open("Sejong-acc.txt", "r", encoding="euc-kr") as f:
    line = f.readline()
    count = 1
    for i in range (1450000):
        plist = line[:-1].split("\t")
        wordlist[plist[-1]] = plist[1]
        line = f.readline()
    plist = line[:-1].split("\t")
    wordlist[plist[3]] = plist[1]
    f.close()
while True:
    sentence = input("문장을 입력하세요 : ")
    if sentence == "quit":
        break
    slist = sentence.split(" ")
    for i in slist:
        if i in wordlist:
            print(str(wordlist[i]) + "% * ", end="")
        else :
            print("0%(없음) * ", end="")
    print("1")
    