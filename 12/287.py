# Проверено - 307

def replacer(s)->tuple:
    leni = len(s)
    while '555' in s or '888' in s:
        s = s.replace('555','8',1)
        s = s.replace('888','55',1)
    return s,leni

i = 301
mas = []

while True:
    s = '8'*i
    i += 1

    new_s = replacer(s)
    if new_s[0] in ('58','85'):
        mas.append(new_s[1])
    
    if i == 10000:
        break

print(min(mas))