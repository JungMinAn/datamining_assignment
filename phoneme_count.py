countlist = [0 for _ in range(11172)]
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
max_count = int(input("가장 많이 등장한 음절들 중 표시할 갯수를 입력하세요 : "))
stacked_per = 0
print("음절 갯수 확률 누적확률")
for i in range(max_count):
    max_value = max(countlist)
    max_index = countlist.index(max_value)
    percentage = round((100 * max_value / count), 4)
    stacked_per += percentage
    print(chr(max_index + 44032) + " : " + str(max_value) + " " + str(percentage) + "% " + str(round(stacked_per, 4)) + "%")
    countlist[max_index] = -1