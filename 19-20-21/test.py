def h(s): return s+1, s*2

def Orig_G(func,Mn=set()):
    return {i for i in s_values if func(j >= 29 for j in h(i))}

def G(func, Mn = set()):
    return {i for i in s_values if func(j in Mn for j in h(i))}

s_values = {i for i in range(1,29)}

winns_1 = Orig_G(any)
lose_1 = G(all, winns_1)
winns_2 = G(any, lose_1)
lose_2 = G(all, winns_2|winns_1)

print(winns_1)
print(lose_1)
print(winns_2)
print(lose_2)
