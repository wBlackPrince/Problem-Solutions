# Проверено - 33

def replacer(s) -> str:
    while '33333' in s or '999' in s:
        if '33333' in s:
            s = s.replace('33333','99',1)
        else:
            s = s.replace('999','3',1)
    return s

s = '9'*84
print(replacer(s))