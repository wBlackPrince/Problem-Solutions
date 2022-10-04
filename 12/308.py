# Проверено - 299

def replacer(s) -> str:
    while '22222' in s or '9999' in s:
        if '22222' in s:
            s = s.replace('22222','99',1)
        elif '9999' in s:
            s = s.replace('9999','2',1)
    return s

s = '9'*96

print(replacer(s))