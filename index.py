def missing_char(word, n):
    if n > len(word):
        return "out of range index"
    else:
        removed_word = list(word)
        removed_word.pop(n)
        new_word = ""
        for i in removed_word:
            new_word += i
        return new_word
print(missing_char("kitchen", 1))
print(missing_char("kitchen", 0))
print(missing_char("kitchen", 4))
print(missing_char("kitchen", 10))
