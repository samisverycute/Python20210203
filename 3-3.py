math=[]
name=[]
total = 0
high = 0
low = 100
n = int(input("How many people in this class"))
for i in range(n):
    stuname = input('Please input the name:')
    score = int(input("Please input the score:"))
    math.append(score)
    name.append(stuname)
    total = total + score
    
for i in range(n):
    if math[i] < low:
        low = math[i]
        lowname = name[i]
for i in range(n):
    if math[i] > high:
        high = math[i]
        highname = name[i]        
average = total / n
print(math)
print("average:",average)
print("high:",high,highname)
print("low:",low,lowname)