def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")

if is_palindrome(word.lower()):
    print(f"{word} is a palindrome")

else: 
    print(f"{word} is not a palindrome.")