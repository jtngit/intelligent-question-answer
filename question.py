import in_and_out as io
import trained_for_que_ans as nw
import data_clean as dc
from nltk.tokenize import sent_tokenize

def questions():

    selected_sentences=[]
    selected_sentences_list=[]
    sentence_dict={}
    sentance_pref={}
    no_sen_pref={}
    sen_pref=[]
    no_sen_pref_list=[]
    l=0


    a = io.tfidf_read()
    tfidf = a[0]
    docs_dict = a[1]
    words_dict = a[2]
    doc_index = a[3]
    doc_path = a[4]

    question = input("enter your Question:")
    print("Your Question is: "+question)

    #### calling clean function for cleaning question
    after_stemming = dc.clean(question)
    no_words_question= len(after_stemming) 

    ###############   creating question contains words thats key value in words_dict ######
    question_word_index = []
    for q in after_stemming:
        #print(q)
        if (q in words_dict):
            question_word_index.append(words_dict[q])
            
    #print(question_word_index)   
    ##################### findind no words in a row of matrix ###############
    no_words_tfidf_matrix= len(words_dict)  
    #print(no_words_tfidf_matrix) 
    ##################### creating list length of row ########################
    matrix_row= [0]*no_words_tfidf_matrix  
    #print(matrix_row)
    #################### counting and locate in position of word #############
    for r in question_word_index:
        matrix_row[r] +=1
    #print(matrix_row)

    no_docs= len(docs_dict)
    ########################## create matrix with all values zero , size = tfidf ##########
    product_tfidf_and_word_matrix=[]
    for rw in range (0,no_docs):
        product_tfidf_and_word_matrix.append([0]*no_words_tfidf_matrix)

    #print(product_tfidf_and_word_matrix)
    ##################### finding matrix question words tfidf value ##################
    for t in range(0,no_docs):
        for y in range(0,no_words_tfidf_matrix):
            product_tfidf_and_word_matrix [t][y]= matrix_row[y] * tfidf[t][y]
            
    #for u in product_tfidf_and_word_matrix:
    print("")
    #    print(u)
        
    ################# document weight in question ###############################
    #print(doc_index)
    doc_weight= {}
    for rw in range(0,no_docs):
        doc_weight.update({float(sum(product_tfidf_and_word_matrix[rw])):doc_index[rw]})
        
    print(doc_weight)
    print("")
    ################### max waited document ####################################
    max_vl_doc = max(doc_weight)
    selected_doc= doc_weight[max_vl_doc]
    print("max doc= "+selected_doc+"      doc value= "+str(max_vl_doc))


    ################# take selected doc ###############################
    fob=open(doc_path+"/"+selected_doc,'r')
    txt=fob.read()
    print(txt)
    fob.close()

    ################# sentence tockenization ############################

    sentences= sent_tokenize(txt)
    for sen in sentences:
        print(sen)

        #################### creating sentence dictionary from selected document #######
        sentence_dict.update({l:sen})

        ####### calling clean function ###################
        after_stemming_doc = dc.clean(sen)

        ###################### (union of question and sentance) / total no of words in question #######
        count= 0
        for que in after_stemming:
            for word in after_stemming_doc:
                if que == word :
                    count +=1
        print("_______________________________")
        print(count)
        print(no_words_question)
        ans= float(count)/float(no_words_question)
        print(ans)
        
        sen_pref.append(ans)
        sentance_pref.update({l:ans})  #####  this is the error using this dictionary
        l +=1

    
    print("@@@@@@@@@@@@@@@@@@@@@ sentence dictionary @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")    
    print("")    
    print(sentence_dict)
    print("_______________$$$$$$$$$$____________________")
    print(sentance_pref)
    print("___________________________________")
    print(sen_pref)
    print("___________________________________")
    sen_pref.sort()
    print(sen_pref)
    print("___________________________________")
    sen_pref.reverse()
    print(sen_pref)
    nm=0
    for sen_p in sen_pref:
        nm +=1
        no_sen_pref.update({sen_p:nm})
    for xyz in no_sen_pref:
        
        if xyz != 0:            
            no_sen_pref_list.append(xyz)
            
    no_sen_pref_list.sort()
    no_sen_pref_list.reverse()
        
    ############### printing sentances in order of preference #########################
    print("")
    print("__________printing sentances in order of preference_______________")
    x=1
    for pref in no_sen_pref_list:
        print("pref: "+str(pref))
        for index_dict in sentance_pref:
            print("index_dict: "+str(index_dict))
            if pref==sentance_pref[index_dict]:
                print("________________________________")
                #print("pref: "+str(pref))
                #print("sentance_pref[index_dict]"+str(sentance_pref[index_dict]))
                print(x)
                
                z= index_dict
                #print(z)
                sen_list =sentence_dict[z]
                senta= "sentance"+str(x)+": "+ sentence_dict[z]
                #print(senta)
                x +=1
                selected_sentences_list.append(str(sen_list))
                selected_sentences.append(str(senta))
    print(no_sen_pref)
    print(no_sen_pref_list)
    print(sen_pref)
    print(sentance_pref)
    print("question: "+str(question))
    print(selected_sentences_list)######## selected sentences

    #nw.question_answer_nurel_network(question,selected_sentences_list)
    selected_sentence= nw.question_answer_nurel_network(question,selected_sentences_list)
   
    return selected_sentence
