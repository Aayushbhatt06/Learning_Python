string = input("Enter a string: ")
string = string.lower()  # Convert the string to lowercase
string = string.strip()  # Remove non-alphanumeric characters

if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
