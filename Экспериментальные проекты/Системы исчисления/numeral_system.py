num = 1234
print("Исходное число в десятичной системе: ", num)

num_2 = bin(num)
print("Число в двоичной системе", num_2)

num_16 = hex(num)
print("Число в шестнадцатиричной системе", num_16)

num_8 = oct(num)
print("Число в восьмеричной системе", num_8)

print("Коды символов:")
for i in str(num).strip():
    num_ord = ord(i)
    print(str(i) + " --> " + str(num_ord))

print("Обратный перевод в десятичную: ", int(num_8,8))