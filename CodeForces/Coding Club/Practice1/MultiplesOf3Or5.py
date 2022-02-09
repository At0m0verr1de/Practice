def answer(maximum, number):
    n = (maximum-1)//number
    return number * n * (n+1)//2
 
 
for _ in range(int(input())):
    num = int(input())
    print(answer(num, 3) + answer(num, 5) - answer(num, 15))
