first, second, third = input().split()
ucode = (44032 + (int(first) * 588) + (int(second) * 28) + int(third))
print(chr(ucode))