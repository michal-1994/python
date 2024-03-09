import csv

file_path = "titanic.csv"
file = open(file_path)
data = [row for row in csv.reader(file)]
file.close()
header = data[0]
data = data[1:]

rows_num = len(data)

class_1 = [row for row in data if row[1] == '1st']
class_2 = [row for row in data if row[1] == '2nd']
class_3 = [row for row in data if row[1] == '3rd']

def print_survival_rate(data):
    count = 0
    survived = 0
    for row in data:
        count += 1
        if row[4] == '1':
            survived += 1
    print(float(survived) / count)

print_survival_rate(class_1)
print_survival_rate(class_2)
print_survival_rate(class_3)