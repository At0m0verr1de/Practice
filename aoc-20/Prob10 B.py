"""
    1. You need to find total number of ways that you can connect the charges together
    2. So like if you have 0, 3, 5, 6, 9 then start with zero index and go forward till you get
        difference > 3 number then counter-1 will be ur possibilities.
    3. so for each selection suppose 2 we need to see how many more selections possible.
    4. You will always have to include the last adaptor so that's not a question.
    5. Let's brute force it lol
"""
import random

dataset = """67
118
90
41
105
24
137
129
124
15
59
91
94
60
108
63
112
48
62
125
68
126
131
4
1
44
77
115
75
89
7
3
82
28
97
130
104
54
40
80
76
19
136
31
98
110
133
84
2
51
18
70
12
120
47
66
27
39
109
61
34
121
38
96
30
83
69
13
81
37
119
55
20
87
95
29
88
111
45
46
14
11
8
74
101
73
56
132
23
0
140""".split("\n")

dataset = list(map(int, dataset))
dataset.sort()

print(dataset)
seq = []
