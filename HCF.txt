num1 = int(input("ENter n1"))
num2 = int(input("enter n2"))

if num1<num2:
    small=num1
else:
    small=num2

while True:
    if num1%small==0 and num2%small==0:
        print("HCF = ",small)
        break
    else:
        small-=1