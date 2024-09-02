def is_palindrome(sequence):
    return sequence == sequence[::-1]

lst = input("Input: ")

result = is_palindrome(lst)
print("Output:", result)