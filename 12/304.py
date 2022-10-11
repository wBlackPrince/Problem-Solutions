def replacer(s):
    while '00' not in s:
        s = s.replace('01','21022',1)
        s = s.replace('02','310',1)
        s = s.replace('03','230112',1)
    return s



for one in range(50):
    for two in range(50):
        for three in range(50):
            s = '0' + one*'1' + two*'2' + three*'3' + '0'
            new_s = replacer(s)
            if new_s.count('1') == 104 and new_s.count('2') == 39 and new_s.count('3') == 83:
                print(len(s))

