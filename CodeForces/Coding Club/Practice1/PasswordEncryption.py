index = 0
num = int(input())
letters = []
 
while num > 0:
    remainder = num % 26
    if remainder == 0:
        letters.append('z')
        num = num//26 - 1
    else:
        letters.append(chr(int(ord('a') + remainder - 1)))
        num = num//26
 
letters.reverse()
 
print("".join(letters))
