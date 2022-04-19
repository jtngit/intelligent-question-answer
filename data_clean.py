from nltk.tokenize import sent_tokenize
    
from nltk.tokenize import word_tokenize
    
from nltk.stem import PorterStemmer 
ps = PorterStemmer()
                    
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

import re

def clean(txt):
    print("@@@@@@@@@@@@@@special character removel@@@@@@@@@@@@@@@@@@")

    specha = re.sub('[^a-zA-Z0-9_ ]', '', txt)
    words=word_tokenize(specha)

    print("     ")  
    print("!!!!!!!!!!!!!! stop word removal !!!!!!!!!!!!!!!!!!")  
    filtered_sentence = []    
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
                    
    print("     ")                      
    print("@@@@@@@@@@@@@@@@@@@@@ stemming @@@@@@@@@@@@@@@@@@@@@")
    ste=[]                   
    for w in filtered_sentence:
        ste.append((ps.stem(w)))

    return ste

def mining_not_avoid_stopwords(txt):
    #print("@@@@@@@@@@@@@@special character removel@@@@@@@@@@@@@@@@@@")

    specha = re.sub('[^a-zA-Z0-9_ ]', '', txt)
    #print(specha)
        
    c=word_tokenize(specha)
                
    #print("@@@@@@@@@@@@@@@@@@@@@ stemming @@@@@@@@@@@@@@@@@@@@@")
    #print("  ")
    ste=[]                   
    for w in c:
        ste.append((ps.stem(w)))
    #print(ste)
    return ste

def type_of_question_word(b):
    count=0
    #print("b= "+str(b))
    question_words={'who':1,'where':2,'when':3,'whi':4,'what':5,'which':6,'how':7, 'whome':8, 'doe':9, 'there':10, 'can':11}
    #print(question_words)
    for i in b:
        #print(i)
        for j in question_words:
            #print(j)
            if i==j:
                #print("question_words"+str(question_words[i]))
                count= question_words[i]
    return count