def F(s,c,m):
    if s >= 34: return c%2 == m%2
    if c == m: return 0

    h = [F(s+1,c+1,m), F(s+2,c+1,m), F(s+3,c+1,m), F(s*2,c+1,m)]

    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1,34):
    for m in range(1,5):
        if F(s,0,m):
            if m == 4:
                print(s, m)
            break

"""
    Стандартная 1 куча
"""
