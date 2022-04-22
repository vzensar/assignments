
#A
n=4
num=1
for i in range(0,n):
    for j in range(0, i+1):
        print(num, end="")
        num+=1
    print("")



n=6
for n in range(n):
    for i in range(n):
        print(n, end="")
    print("")





a=5
for i in range(1,a+1):
    print(" "*(a-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range((a-1),0,-1):
    print(" "*(a-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()



