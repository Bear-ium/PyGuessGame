import random

def Generate(maxN: int) -> int:
    if maxN > 1:
        return random.randint(1,maxN)
    else:
        return 0