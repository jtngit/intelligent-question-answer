
import data_clean as dc
import trained_network as sl
import pickle   
import numpy as np

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
    pickle_variable = open('answers.list', 'wb')
    pickle.dump(answers, pickle_variable)
    pickle_variable.close()
    
    array= [] 
    cc= []
    gg= []
    ques= question  
    
    ans= answers
    print(ans)
    print("")
    print(ques)
    no_answ= len(ans)
    for i in range(0,no_answ):
        #print("____________________")
        #print("question: "+str(ques))
        m= ans[i]
        print("")
        print("answer"+str(i)+": "+str(m))
        type_question_words= dc.mining_not_avoid_stopwords(ques)
        print("mining_not_avoid_stopwords: "+str(type_question_words))
        question_words=dc.clean(ques)
        print("mined question_words: "+str(question_words))
        answer_words= dc.clean(m)
        print("mined answer_words: "+str(answer_words))
        
        question_array=[]
        
        
        #print("words= "+str(question_words))
        question_word_value=dc.type_of_question_word(type_question_words)
        print("question_words= "+str(question_word_value))
        question_array.append(question_word_value)
        
        count_commen_words= no_commen_words(question_words,answer_words)
        print("count_commen_words= "+str(count_commen_words))
        question_array.append(count_commen_words)
        
        count_diff_words= no_diff_words(question_words,answer_words)
        print("count_diff_words= "+str(count_diff_words))
        question_array.append(count_diff_words)
        
        words_ratio= ratio(question_words,answer_words)
        print("words_ratio= "+str(words_ratio))
        question_array.append(words_ratio)
        
        print(question_array)
        array.append(question_array)
    print("array"+str(array))
    
    pkl_file = open('dividing_values.list', 'rb')
    
    dividing_values = pickle.load(pkl_file)
        
    pkl_file.close()
    
    print("dividing_values= "+str(dividing_values))
    for arr in array:
    
        roww= np.array(arr)
        print("______________________________________________")
        print(roww)
        div_roww= np.array(dividing_values)
        divided_row= roww/div_roww
        print("divided_row"+str(divided_row))
        #print("divided_row=  "+str(divided_row))
        cc.append(divided_row)
        gg= np.array(cc).tolist()
        print("gg= "+str(gg))

    result=sl.learn(gg)
    return(result)

