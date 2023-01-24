from functools import lru_cache

@lru_cache(None)
def main(s1,s2):
    if sum([s1,s2]) >= 77: return False

    moves = [main(s1+1,s2), main(s1,s2+1), main(s1*2,s2),  main(s1,s2*2)]
    lose_steps = [i for i in moves if i <= 0]
    if lose_steps:
        return -max(lose_steps) + 1
    else:
        return -max(moves)

for i in range(1,70):
    print(i, main(7,i))