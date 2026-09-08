from typing import List

def read_integers() -> List[int]:
    a = [int(x) for x in input().split(",")]
    return a

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
