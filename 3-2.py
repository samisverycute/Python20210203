a=[]
s = 0
d = 0
f = 100
n = int(input("How many people in this class"))
for i in range(n):
    score = int(input("Please input the score"))
    s = s+score
    if d < score:
        d = score
    if f > score:
        f = score
    a.append(score)
average = s / n
print(a)
print("average:",average)
print("high:",d)
print("low:",f)