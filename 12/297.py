# Проверено - МОНИТОР

a = 'ВИАНДОТ'
i = len(a)
b = 'М'

while i > 1:
    c = a[i-2]
    b += c
    i -= 2
b += 'ТОР'
print(b)