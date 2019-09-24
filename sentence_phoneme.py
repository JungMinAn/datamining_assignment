countlist = [1 for _ in range(11172)]
count = 0
data_len = int(input("검사 할 음절의 총 갯수를 입력하세요 : "))
with open("ko_wiki_text_EUCKR-utf16.txt", "rb") as f:
    byte = f.read(2)
    while count < data_len and byte != b"":
        byte = f.read(2)
        phoneme = byte.decode("utf-16le")
        ucode = ord(phoneme)
        if 44032 <= ucode and ucode < 55204 :
            countlist[ucode-44032] = countlist[ucode-44032] + 1
            count += 1
    f.close()

while True:
    sentence = input("문장을 입력하세요 : ")
    if sentence == "quit":
        break
    for i in sentence:
        icode = ord(i)
        if 44032 <= icode and icode < 55204 :
            icode -= 44032
            iper = round((100 * countlist[icode] / count), 4)
            print(str(iper) + "% *" ,end=" ")
    print("1")