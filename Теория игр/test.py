def f(s,c,m):
    if s >= 30: return c%2 == m%2
    if c == m: return 0

    h = [f(s+2,c+1,m), f(s+3,c+1,m), f(s*2,c+1,m)]
    return any(h) if (c+1)%2 else all(h)