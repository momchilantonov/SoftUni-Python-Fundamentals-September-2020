list_of_words = input().split()
searched_palindrome = input()

list_of_palindromes = [word for word in list_of_words if word == word[::-1]]

for palindrome in list_of_palindromes:
    list_of_palindromes.count(searched_palindrome)

print(list_of_palindromes)
print(f"Found palindrome {list_of_palindromes.count(searched_palindrome)} times")