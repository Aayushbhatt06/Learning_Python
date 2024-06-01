num = str(input("Enter a number"))
a = len(num)
b = int(num)
decimal=0
for j in range(0,a):
    d=(b//10**j)%10
    decimal+=d*2**j
print(decimal)