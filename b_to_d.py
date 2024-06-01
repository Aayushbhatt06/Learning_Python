# str1 = input("string = ")
# str1.lower().replace(" ","")

# if str1==str1[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

string = input("Enter a string: ")
string = string.lower()  # Convert the string to lowercase
string = string.strip()  # Remove non-alphanumeric characters

if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
