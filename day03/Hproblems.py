#1
# 1.Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60,7:70}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)
print("-"*40)

#2
# 2.Write a Python script to check whether a given key already exists in a dictionary

d1={'x':10,'y':20,'z':30}
if 'x' in d1:
    print("key presented")
else:
    print("not presented")
print("-"*40)

#3
#3. Write a Python program to iterate over dictionaries using for loops.
d={'a':'apple','b':'ball','c':"cat"}
for key ,value in d.items():
    print(key,value)

print("-"*40)

#4
# 4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
N=5
dict=dict()
for i in range(1,N+1):
    dict[i]=i*i
    print(dict)

print("-"*40)

#5
#5. Write a Python program to remove duplicates (values) from Dictionary
dict={'a':20,'b':30,'c':40,'d':50}
if 'a' in dict:
    del dict['a']
    print(dict)
print("-"*40)

#6
#6. Write a code to get the key of a minimum value from a dictionary
test_dict={'A':11,'B':22,'C':33,'D':44}
print(min(test_dict,key=test_dict.get))
print("-" * 40)

#7
#7. Reverse a list in Python
list=[1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)
print("-" * 40)

#8

#8. Remove all occurrences of a specific item from a list.
i=[1,2,3,0,4,5,0,7,8,9,0]
val=0
try:
    while True:
        i.remove(val)
except ValueError:
    pass
print(i)
print("-" * 40)

#9
#9. Write a Python program to sum all the items in a list
list1=[1,2,3,4,5,6,7,8,9]
total=sum(list1)
print(f"total:{total}")

print("-"*40)

#10
#10. Write a Python program to get the second largest number from a list
list=[10,20,30,40,10,60,55,50]
list.sort()
print(list)
print(list[-2])
print("-" * 40)

#11
#11. Write a Python program to find the second smallest number in a lis
list=[10,20,30,40,60,55,50]
list.sort()
print(list[1])
print("-" * 40)

#12
#12. Write a Python program to get unique values from a list.
list=[11,22,33,44,33,53,40,11]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)
print("-" * 40)

#13
#13. Write a Python program to get count of repetition of each value from a list.
list=[11,22,33,44,34,33,53,40,33]
N=33
count=0
for element in list:
    if(element==N):
        count=count+1
print(count)
print("-" * 40)

#14
#14. Write a Python program to find common items from two lists.
def matchele():
    list1=[1,2,3,4,5,6]
    list2=[4,5,6,7,8,9]
    for i in list1:
        for j in list2:
            if i == j:
                print(i)
matchele()

print("-" * 40)

#15
#15. Write a Python program to count number of lists in a list of lists.
def list_count(list_A):

    return len(list_A)

list_A=[[1,3],[5,7],[7,8]]
print(list_count(list_A))





