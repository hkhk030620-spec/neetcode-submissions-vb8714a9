def add_two_numbers() -> int:
    x=input()
    l=x.split(",")
    m=[]
    for i in l:
        m.append(int(i))
    return m[0]+m[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
