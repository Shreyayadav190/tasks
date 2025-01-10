def is_palindrome(s):

    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
