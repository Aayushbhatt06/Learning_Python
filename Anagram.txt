str1=str(input("Enter the string"))
str2=str(input("Enter the string"))

str1=str1.lower().replace(" ","")
str2=str2.lower().replace(" ","")

if sorted(str1)==sorted(str2):
    print("its an anagram")
else:
    print("its not a anagram")