length = int(input())
 
array1 = input().split()
array2 = input().split()
 
array1.sort()
array2.sort()
found = False
 
for i in range(0, length):
    if array1[i] != array2[i]:
        print("No")
        found = True
        break
 
 
if not found:
    print("Yes")
