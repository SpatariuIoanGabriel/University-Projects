n = int(input("Read a number:"))
for i in range(0, n + 1):
    sum_digits = 0
    copy_i = i
    while copy_i != 0:
        sum_digits += copy_i % 10
        copy_i = copy_i // 10
    if sum_digits + i == n:
        print("True")
        break
else:
    print("False")