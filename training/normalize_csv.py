#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:18:52 2018

@author: justine
"""
import csv
import numpy as np
import pickle
#import csv
'''import pandas as pd
df = pd.read_csv("flow.csv", header=None, names=["type","commen","diff","ratio"])
print(df.columns['commen'])'''

typeq = []
diff = []
ratio = []
commen = []
dividing_values = []
b=[]
c=[]
z=[]


f = open( 'flow.csv', 'rU' ) 
print(str(f))
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
for line in f:
    cells = line.split( "," )
    typeq.append( int( cells[ 0 ] ) ) 
    diff.append( int( cells[ 1 ] ) )
    ratio.append( int( cells[ 2 ] ) )
    commen.append( float( cells[ 3 ] ) )    
f.close()


z.append(typeq) 
z.append(diff)
z.append(ratio)
z.append(commen)


#print typeq
typeq_max=max(typeq)
typeq_min=min(typeq)
#print(typeq_max)
#print(typeq_min)
typeq_val=typeq_max-typeq_min
#print("typeq_val= "+str(typeq_val))
dividing_values.append(typeq_val)


#print diff
diff_max=max(diff)
diff_min=min(diff)
#print(diff_max)
#print(diff_min)
diff_val=diff_max-diff_min
#print("diff_val= "+str(diff_val))
dividing_values.append(diff_val)

#print ratio
ratio_max=max(ratio)
ratio_min=min(ratio)
#print(ratio_max)
#print(ratio_min)
ratio_val=ratio_max-ratio_min
#print("ratio_val= "+str(ratio_val))
dividing_values.append(ratio_val)

#print commen
commen_max=max(commen)
commen_min=min(commen)
#print(commen_max)
#print(commen_min)
commen_val=commen_max-commen_min
#print("commen_val= "+str(commen_val))
dividing_values.append(commen_val)

print("dividing_values"+str(dividing_values))

pickle_variable = open('dividing_values.list', 'wb')
    
pickle.dump(dividing_values, pickle_variable)
pickle_variable.close()


print("###########################################################")
#print("z= "+str(z))
#d = np.array(a)

    
    
      
d90= np.transpose(z)
#print("d90= "+str(d90))
aa=np.array(d90).tolist()
print(aa)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
for m in aa:
    #b.append(m)
    #print("b"+str(b))
    roww= np.array(m)
    div_roww= np.array(dividing_values)
    divided_row= roww/div_roww
    #print("divided_row=  "+str(divided_row))
    c.append(divided_row)
    g= np.array(c).tolist()
    #print(b)
    #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    
#a=[]
#print("b= "+str(b))
#print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#print("c= "+str(c))
#print("____________________________________________________")
#print("g= "+str(g))

"""for li in g:
    
    print(li)
    
    file= open("normalize.csv","a")
    k=0
    while k<len(li):
        
        print("value:"+str(li[k]))
        #file.write(str(li[k])+",")
        file.write(str(li[k])+",")
        k=k+1
    file.writelines("\n")
    print("__________________________________")
file.close"""

with open('bef_eggs.csv','w') as csvfile:
    
    spamwriter = csv.writer(csvfile, delimiter=',',lineterminator = '\n')
    for li in g:
        print(li)
        print("__________________________________")
                                
        spamwriter.writerow(li)

"""with open('flow.csv') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         print ','.join(row)
         print(row)

'''with open('flow.csv') as csvfile:
   readCSV = csv.reader(csvfile, delimiter=',')
   for row in readCSV:
       print(row)
       row.pop()
       print(row)
       
       a.append(row)
       print("____________________________________________________")
       
       #print(row[1])
        #print(row[0],row[1],row[2],)'''
#print(a)
print("input"+str(a))
b = map(float, a)
print("b= "+str(b))"""





