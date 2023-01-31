from functools import lru_cache

@lru_cache(None)
def main(s1):
    if s1 >= 25: return 0

    steps = [main(s1+1), main(s1*2)]
    negative = [i for i in steps if i <= 0]

    if negative:
        return abs(max(negative)) + 1
    else:
        return -max(steps)

for i in range(1,19):
    print(i, main(i))