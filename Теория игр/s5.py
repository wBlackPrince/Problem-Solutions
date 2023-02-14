def F(s1,s2,c,m):
    if (s1 + s2) >= 68: return c%2 == m%2
    if c == m: return 0

    h = [F(s1+1,s2,c+1,m), F(s1,s2+1,c+1,m), F(s1+s2,s2,c+1,m), F(s1,s2+s1,c+1,m)]
    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1,59):
    for m in range(1,5):
        if F(8,s,0,m):
            if m == 4:
                print(s,m)
            break

"""
    2 кучи с нестандартным ходом
"""