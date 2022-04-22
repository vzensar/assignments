
a=int(input("enter any number"))    #40585
g=a
fact=1
sum=0
while(a>0):
    r=a%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
    a=a//10
if(sum==g):
    print("satisfy number")
else:
    print("not")

print("-"*40)

# fact=1
# sum=0
# while(a>0):
#     r=a%10
#     fact=1
#     for i in range(1,r+1):
#         fact=fact*i
#     sum=sum+fact
#     a=a//10
# print(fact)
'''
def fac(n):
    if n==1:
        return 1
    else:
        return  n * fac(n-1)
n=int(input("enter number:"))
print(f" the factorial of (n) is : {fac(n)}")
'''