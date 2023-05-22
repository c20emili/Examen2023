import csv

i = csv.reader(open('DemoA2.csv', 'r'))
o = open("A2.csv", 'w')
nr = 1
for row in i:
    o.write(str(nr)+','+row[1]+'\n')
    nr += 1
