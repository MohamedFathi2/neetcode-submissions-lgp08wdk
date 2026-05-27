def add_two_numbers() -> int:
    s_in = input().split(',')
    _sum = 0
    for x in s_in:
        _sum += int(x)
    return _sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
