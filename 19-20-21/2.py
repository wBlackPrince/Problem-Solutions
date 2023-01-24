from functools import lru_cache

@lru_cache(None)
def main(s1,s2):
    if sum([s1,s2]) >= 83: return 0

    steps = [main(s1+1, s2), main(s1, s2+1), main(s1*2, s2), main(s1, s2*2)]
    negative = [i for i in steps if i <= 0]

    if negative:
        return abs(max(negative)) + 1
    else:
        return -max(steps)


for i in range(1,83):
    print(i, main(9,i))

# 19 - 19 (заменить max на min)
# 20 - 32, 36
#21 - 31