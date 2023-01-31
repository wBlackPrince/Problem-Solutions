def h(s1, s2): return (s1+1,s2), (s1, s2+1), (s1*2,s2), (s1, s2*2)

def Orig_G(func,Mn=set()):
    return {i for i in s_values if func(sum(j) >= 61 for j in h(10,j))}

def G(func, Mn = set()):
    return {i for i in s_values if func(j in Mn for j in h(10,i))}

s_values = {(10,a) for a in range(1,60) if a+10 < 61}

winns_1 = Orig_G(any)
lose_1 = G(all, winns_1)
winns_2 = G(any, lose_1)
lose_2 = G(all, winns_2|winns_1)

print(winns_1)
print(lose_1)
print(winns_2)
print(lose_2)
