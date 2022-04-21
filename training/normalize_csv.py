import csv
import numpy as np
import pickle

typeq = []
diff = []
ratio = []
commen = []
crt_or_wrong = []
dividing_values = []
b=[]
#c=[]
g=[]
z=[]


f = open( 'flow.csv', 'r' ) 
for line in f:
    cells = line.split( "," )
    typeq.append( int( cells[ 0 ] ) ) 
    diff.append( int( cells[ 1 ] ) )
    ratio.append( int( cells[ 2 ] ) )
    commen.append( float( cells[ 3 ] ) )
    crt_or_wrong.append(int( cells[ 4 ] ))
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

#print("dividing_values"+str(dividing_values))

pickle_variable = open('dividing_values.list', 'wb')
    
pickle.dump(dividing_values, pickle_variable)
pickle_variable.close()

#print(z)
d90= np.transpose(z)
#print("d90= "+str(d90))
aa=np.array(d90).tolist()
#print(aa)
#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
j=0
for m in aa:
    #print("b"+str(b))
    roww= np.array(m)
    div_roww= np.array(dividing_values)
    divided_row= roww/div_roww
    #print("divided_row=  "+str(divided_row))

    #c=[]
    rows=[]
    #c.append(np.array(divided_row).tolist())
    #print(f"printing c = {c}")


    ############### adding 1 & 0 at the end of list ####################
    for val in divided_row:
        rows.append(val)
    rows.append(crt_or_wrong[j])
    j= j+1
    # print(rows)

    # print("__________________________________")
    g.append(rows)
    
    




    # c.append(divided_row)

    # #adding 1 & 0 at the end of list
    # c.append(crt_or_wrong[j])
    # print(c)
    # print("__________________________________")

    # g= np.array(c).tolist()

with open('eggs.csv','w') as csvfile:
    
    spamwriter = csv.writer(csvfile, delimiter=',',lineterminator = '\n')
    for li in g:
        #print(li)
        #print("__________________________________")
                                
        spamwriter.writerow(li)
