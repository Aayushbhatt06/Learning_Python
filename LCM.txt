num1 = int(input("ENter n1"))
num2 = int(input("enter n2"))

if num1>num2:
    greater=num1
else:
    greater=num2

while True:
    if greater%num1==0 and greater%num2==0:
        print("LCM=",greater)
        break
    else:
        greater+=1