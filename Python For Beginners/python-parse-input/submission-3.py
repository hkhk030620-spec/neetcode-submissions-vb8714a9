from typing import List

def read_integers() -> List[int]:
    x=input()
    l=[]
    for i in x.split(","):
        l.append(int(i))

    return l

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
