with open('27-1a.txt','r') as fa,open('27-1b.txt','r') as fb:
    # избавление от разделиетелей
    file_a = [i.rstrip('\n') for i in fa.readlines()]
    file_b = [i.rstrip('\n') for i in fb.readlines()]

file_a = [(i[:i.find(' ')],i[i.find(' ')+1:]) if ' ' in i else i for i in file_a]
file_b = [(i[:i.find(' ')],i[i.find(' ')+1:]) if ' ' in i else i for i in file_b]
