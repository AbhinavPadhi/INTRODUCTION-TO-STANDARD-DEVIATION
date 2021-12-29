import csv
import math

with open('data3.csv', newline='') as a:
    reader = csv.reader(a)
    filedata = list(reader)

data = filedata[0]

def mean(data):
    n = len(data)
    total = 0
    for a in data:
        total += int(a)
    mean = total / n

    return mean

list = []
for number in data:
    a = int(number) - mean(data)
    a = a ** 2

    list.append(a)

sum = 0
for b in list:
    sum = sum + b

result = sum / (len(data) - 1)

standardDeviation = math.sqrt(result)

print(standardDeviation)
