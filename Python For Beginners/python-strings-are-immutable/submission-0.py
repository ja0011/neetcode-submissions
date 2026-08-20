def remove_fourth_character(word: str) -> str:
    a = word[:3]
    b = word[4:]

    return(a + b)


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
