
def create_palindrome(word):
    # Reverse the input word and concatenate it with the original word
    palindrome = word [::-1]
    return palindrome

# Example usage
input_word = input("Enter a word: ")
result = create_palindrome(input_word)
print("Palindrome:", result)
# create a function to give the longest string in a list of items
def find_longest_string(items):
    longest_string = ''
    for item in items:
        if isinstance(item, str) and len(item) > len(longest_string):
            longest_string = item
    return longest_string

# Example usage
my_list = ['apple', 'banana', 'kiwi', 'orange', 'grapefruit']
result = find_longest_string(my_list)
print("Longest string:", result)
