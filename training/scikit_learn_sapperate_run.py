#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 09:43:29 2018

@author: justine
"""
#import csv
import pickle
import numpy as np
#import matplotlib.pyplot as plt
#import sklearn.linear_model.perceptron as p
from sklearn.linear_model import perceptron
 
# Needed to show the plots inline
#%matplotlib inline
# Data
typeq = []
diff = []
ratio = []
commen = []
crt_wrong= []
z=[]

f = open( 'eggs.csv', 'r' ) 
for line in f:
    cells = line.split( "," )
    typeq.append( float( cells[ 0 ] ) ) 
    commen.append( float( cells[ 1 ] ) )
    diff.append( float( cells[ 2 ] ) )
    ratio.append( float( cells[ 3 ] ) ) 
    crt_wrong.append( int( cells[ 4 ] ) )
f.close()


z.append(typeq) 
z.append(commen)
z.append(diff)
z.append(ratio) 
#z.append(ratio)  
print(f"z= {str(z)}")

d90= np.transpose(z)
print("d90= "+str(d90))
aa=np.array(d90).tolist()     
                
print("input"+str(aa))
d = np.array(aa)
#j = np.transpose(input)
print("")
#print(j)
 
# Labels
t = np.array(crt_wrong)
print("answer: "+str(t))


#print("________________________________")
print("d"+str(d))
print("________________________________")


net = perceptron.Perceptron(max_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)

net.fit(d,t)
print("$$$$$$$$$$$$$$$$$$$$")
########$$$$$$$$$$$$$$$$$$$$$$$$$$#####################################


   
pickle_variable = open('trained.network', 'wb')

pickle.dump(net, pickle_variable)

pickle_variable.close()

############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print("___________________________________________________________")
   
    
    
   