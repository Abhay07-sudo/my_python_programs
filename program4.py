import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(f"'{word}' is a Python keyword.")
else:
    print(f"'{word}' is NOT a Python keyword.")
