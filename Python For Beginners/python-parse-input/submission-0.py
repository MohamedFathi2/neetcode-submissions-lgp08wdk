from typing import List

def read_integers() -> List[int]:
    s = input()
    s_l = s.split(',')
    n_l = []
    for x in s_l: n_l.append(int(x))
    return n_l


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())