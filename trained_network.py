
import pickle
def learn(array):
    
    pkl_file = open('trained.network', 'rb')        
    net = pickle.load(pkl_file)                
    pkl_file.close()
    
    pkl_file = open('answers.list', 'rb')        
    answer = pickle.load(pkl_file)                
    pkl_file.close()
    print("answer= "+str(answer))
    
    selected_sentences=[]
    j=0

    c=net.predict(array)
    print("predict: "+str(c))
    
    m=0
    for k in c:

        if k==1:
            j +=1 
            senta= "sentance"+str(j)+": "+ answer[m]
            #print(senta)
            selected_sentences.append(str(senta))
        m +=1
     
    return selected_sentences