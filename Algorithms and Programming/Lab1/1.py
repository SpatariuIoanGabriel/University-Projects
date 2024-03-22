x = int(input("x="))
while x > 9:
    s = 0
    while x > 0:
        s = s + int(x % 10)
        x = x // 10
    x = s
print(s)