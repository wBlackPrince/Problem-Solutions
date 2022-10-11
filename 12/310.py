# Проверено - 2212122

# осуществляет замены
def replacer(s) -> str:
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111','22',1)
        else:
            s = s.replace('222','11',1)
    return s

# хранилище строк
strings_length = []

# основной цикл
for i in range(204):
    s = '1'*(203-i) + '2' + '1'*(i)
    strings_length.append(replacer(s))

# сортировка по длине и поиск максимальной по длине строки
strings_length = sorted(strings_length,key = lambda x:len(x))
print(strings_length[-1])