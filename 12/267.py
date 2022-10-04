# Проверено - 21

def replacer(s)->str:
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01','302',1)
        s = s.replace('02','3103',1)
        s = s.replace('03','20',1)
    return s


for one in range(50):
    for two in range(50):
        for three in range(50):
            s = '0'+'1'*one + '2'*two + '3'*three
            new_s = replacer(s)
            if new_s.count('1') == 18 and new_s.count('2') == 39 and new_s.count('3') == 25:
                print(s.count('3'))