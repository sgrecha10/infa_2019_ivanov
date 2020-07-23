y = int(input("Enter int: "))

x = y // 2

while x>1:
    if y%x == 0:
        print(y, "имеет делитель", x)
        break
    x -= 1

else:
    print(y, "простое число")
