num=int(input("enter number = "))
order=len(str(num))
sum=0
i=0
while i<order:
    digit=(num//10**i)%10
    sum+=digit**order
    i+=1
if num==sum :
    print("the number is Armstrong number")
else:
    print("the number is not a armstrong number")