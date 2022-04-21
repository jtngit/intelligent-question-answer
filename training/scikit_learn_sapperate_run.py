
import pickle
import numpy as np
#from sklearn.linear_model import perceptron
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


 
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

d90= np.transpose(z)
#print("d90= "+str(d90))
aa=np.array(d90).tolist()     

d = np.array(aa)
print("input"+str(d))
 
# Labels
t = np.array(crt_wrong)
print("answer: "+str(t))


# net = perceptron.Perceptron(max_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)

clf = make_pipeline(StandardScaler(), SVC())

# net.fit(d,t)
clf.fit(d, t)

print("Training successful !!!!")
print(clf.score(d,t))

####### save the trained network ################# 

pickle_variable = open('trained.network', 'wb')
pickle.dump(clf, pickle_variable)
pickle_variable.close()
