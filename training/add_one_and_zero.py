import csv

j = 0
b =[]
f = open( 'bef_eggs.csv', 'r' ) 
for line in f:
    a= []
    for i in line.split(','):
        #print(i)
        a.append(float(i))
        #print(a)

    #print(type(a))
    #print(a)

    j = j+1
    #print(a)
    if (j%2 == 0):
        #print("hi")
        a.append(0)
        #print(a)
        b.append(a)
        print(b)
        
        print("_________________________")

    else:
        #print("hello")
        a.append(1)
        #print(a)
        b.append(a)
        print(b)
        print("_________________________")

f.close()

with open('eggs.csv','w') as csvfile:
    
    spamwriter = csv.writer(csvfile, delimiter=',',lineterminator = '\n')
    for li in b:
        print(li)
        print("__________________________________")
                                
        spamwriter.writerow(li)