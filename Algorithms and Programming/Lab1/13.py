n = input("Read number:")
m = 0
for i in range(0, len(n), 2):
    m = m * 10 + int(n[i])
print(m)
