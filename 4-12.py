def long_words(n):
    word_len = []
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
txt = ['quick', 'brown', 'fox', 'jump', 'over', 'dog', 'lazy']
print(long_words(3))
