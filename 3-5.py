names = []
scores = []

def average(scores):
    total = 0
    for i in range(len(scores)):
        total = total+scores[i]
        ave = total / len(scores)
        return ave
def highest(scores,names):
    high = 0
    temp = []
    for i in range(len(scores)):
        if scores[i] > high:
            high = scores[i]
            highname = names[i]
    temp.append(highname)
    temp.append(high)
    return temp
def lowest(scores,names):
    low = 100
    temp = []
    for i in range(len(scores)):
        if scores[i] < low:
            temp = []
            for i in range(len(scores)):
                if scores[i] < low:
                    low = scores[i]
                    lowname = names
            temp.append(lowname)
            temp.append(low)
            return temp
people = int(input("How many people in this class?"))
for i in range(people):
    n = input("Please input the name:")
    names.append(n)
    s = int(input("SCORE:"))
    scores.append(s) 
print(names)
print(scores) 
a = average(scores)
hi = highest(scores.names) 
lo = lowest(scores.names)
print("The average is",a)
print(hi[0], "got the hirhest score",hi[1])
print(lo[0], "got the lowest score",lo[1])  