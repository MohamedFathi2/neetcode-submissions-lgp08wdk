def remove_fourth_character(word: str) -> str:
    b_f = word[:3]
    a_f = word[4:]
    return b_f + a_f


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
