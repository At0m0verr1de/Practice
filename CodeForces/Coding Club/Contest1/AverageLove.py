length = int(input())
 
array = list(map( int, input().split()))
array.sort(reverse=True)
sum = 0
 
for i in range(0, length):
    sum += array[i]/(2**(i+1))
 
sum += array[-1]/(2**length)
 
print(sum)
