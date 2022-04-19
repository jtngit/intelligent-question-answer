#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:48:27 2018

@author: justine
"""
#import trained_network as sl
#import scikit_learn as sl
#from nltk.tokenize import sent_tokenize 
#import pickle   
from nltk.tokenize import word_tokenize
    
from nltk.stem import PorterStemmer 
ps = PorterStemmer()
                    
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

import re

#import numpy as np
def mining(tx):
    #print("@@@@@@@@@@@@@@special character removel@@@@@@@@@@@@@@@@@@")

    specha = re.sub('[^a-zA-Z0-9_ ]', '', tx)
    #print(specha)
        
    words=word_tokenize(specha)
    #print(len(words))
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
    #print("!!!!!!!!!!!!!! stop word removal !!!!!!!!!!!!!!!!!!")  
    #print("     ")      
    filtered_sentence = []
                             
                
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
                            
    #print(filtered_sentence)
    #print("     ") 
                                
    #print("@@@@@@@@@@@@@@@@@@@@@ stemming @@@@@@@@@@@@@@@@@@@@@")
    #print("  ")
    ste=[]                   
    for w in filtered_sentence:
        ste.append((ps.stem(w)))
        #print(ste)
    return ste
    
def mining_not_avoid_stopwords(txt):
    #print("@@@@@@@@@@@@@@special character removel@@@@@@@@@@@@@@@@@@")
    #print(txt)

    specha = re.sub('[^a-zA-Z0-9_ ]', '', txt)
    #print(specha)
        
    c=word_tokenize(specha)
    #print(len(words))
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
    #print("!!!!!!!!!!!!!! stop word removal !!!!!!!!!!!!!!!!!!")  
    #print("     ")      
    #filtered_sentence = []
                             
                
    #for w in words:
        #if w not in stop_words:
         #   filtered_sentence.append(w)
                            
    #print(filtered_sentence)
    #print("     ") 
                                
    #print("@@@@@@@@@@@@@@@@@@@@@ stemming @@@@@@@@@@@@@@@@@@@@@")
    #print("  ")
    ste=[]                   
    for w in c:
        ste.append((ps.stem(w)))
    #print(ste)
            
           # doc_no_word.append(len(ste))             
            #print(matrix)
            #for i in range (0,1):
             #   matrix[i].append(0)
           # print(matrix)
    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            
            #print(matrix)
             
    #for word in ste:
        #print(word)
    return ste

def type_of_question_word(b):
    count=0
    print("@@@@@@@ question = "+str(b))
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

def no_commen_words(question,answer):
    coun=0
    #print(question)
    #print(answer)
    for qu in question:
        for ans in answer:
            if qu==ans:
                coun +=1
                #print(coun)
    return coun
                
def no_diff_words(question,answer):
    cou=0
    no_words=len(answer)
    for qu in question:
        for ans in answer:
            if qu==ans:
                cou +=1
                #print(coun)
    diff_words= no_words-cou
    return diff_words

def ratio(question,answer):
    no_words_question= len(question)
    #print(no_words_question)
    no_words_answer  = len(answer)
    #print(no_words_answer)
    rat= float(no_words_answer)/float(no_words_question)
    return rat
    
            
def question_answer_nurel_network(question,answers):
    #pickle_variable = open('answers.list', 'wb')
    #pickle.dump(answers, pickle_variable)
    #pickle_variable.close()
    
    array= []    
    ques= question[0]  
    
    ans= answers
    #print(ans)
    print("")
    print("")
    print(ques)
    print("")
    #print(ans)
    no_answ= len(ans)
    #print("no_answ= "+str(no_answ))
    for i in range(0,no_answ):
        #print("____________________")
        #print("question: "+str(ques))
        m= ans[i]
        print("")
        print("answer"+str(i)+": "+str(m))
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        type_question_words= mining_not_avoid_stopwords(ques)
        print("mining_not_avoid_stopwords: "+str(type_question_words))
        question_words=mining(ques)
        #print("mined question_words: "+str(question_words))
        answer_words= mining(m)
        #print("mined answer_words: "+str(answer_words))
        
        question_array=[]
        
        
        #print("words= "+str(question_words))
        question_word_value=type_of_question_word(type_question_words)
        #print("question_words= "+str(question_word_value))
        question_array.append(question_word_value)
        
        count_commen_words= no_commen_words(question_words,answer_words)
        #print("count_commen_words= "+str(count_commen_words))
        question_array.append(count_commen_words)
        
        count_diff_words= no_diff_words(question_words,answer_words)
        #print("count_diff_words= "+str(count_diff_words))
        question_array.append(count_diff_words)
        
        words_ratio= ratio(question_words,answer_words)
        #print("words_ratio= "+str(words_ratio))
        question_array.append(words_ratio)
        
        #print(question_array)
        array.append(question_array)
    print("array"+str(array))
    ######################### sentences training inpuut saved to csv file #############
    for li in array:
        #print(li)
        #print("__________________________________")
        file= open("flow.csv","a")
        k=0
        while k<len(li):
            
            #print("value:"+str(li[k]))
            #file.write(str(li[k])+",")
            file.write(str(li[k])+",")
            k=k+1
        file.writelines("\n")
    file.close
    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
    #sl.learn(array)
    return array
    #transpose_question_array= np.transpose(array)
    #print("transpose_question_array: "+str(transpose_question_array))
