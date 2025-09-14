#simple array
arr=[1,2,3,4,5]
for i in arr:
    print(i, end= ' ')

print( arr[2])

#taking input from user
from array import array
n=int(input("enter size of the array you want to create"))
arr=array('i')
print(f"enter {n} elements into your array")
for i in range(n):
    ele=int(input())
    arr.append(ele)
print("max element in array is:", max(arr))
print("min element in array is :", min(arr))
total=sum(arr)
print('sum of the array is:',total)

#basics operations
arr=[1,10,200,300,20]
print(arr[2])
arr.remove(10)
print(arr)

#search 
arr=[1,2,2,3,4]
if 1 in arr:
    print("found")
else:
    print("not found")

#insertions
arr=[1,2,3,4,5,77,89]
arr.insert(1,125)
print(arr)

#rev
arr=[1,23,45]
print(arr[::-1])
