import csv

i = csv.reader(open('TestDataA-Frame.csv', 'r'))
o = open("TestDataA-Frame2.csv", 'w')
nr = 1
for row in i:
    o.write(str(nr)+','+row[1]+'\n')
    nr += 1
