dataset = """
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29 
38 17 16 15 14 13 30
37 36 35 34 33 32 31
"""

# 0 - 1
# 1 - 3 .... 500 - 1001

# 1 - 2
# 2 - 4 ..... 500 - 1000

#
sum = 0

for j in range(1, 501):
    sum += (2*j + 1)**2  # NE
    sum += (2*j - 1)**2 + (j*2)  # SE
    sum += ((2*j)**2 + 1)  # SW
    sum += ((2*j)**2) + (2*j+1)  # NW

#  We can also just make a function in terms of n where n(1-500) is the row number
#  from 1 (which we treat as row 0)

print(sum+1)

