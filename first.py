import in_and_out as io
import data_clean as dc
import pgm_operations as pgm
import os

matrix=[]


def runstart(doc_path):
    no_of_txt_files = io.find_no_doc_file(doc_path)
    print(no_of_txt_files)

    ## create list of list of value 0
    for g in range(0,no_of_txt_files):
        matrix.append([0]*1)

def doc_clean_and_tfidf(doc_path):
    index_word={}
    index_file={}
    doc_index={}
    j=0
    k=0
    arr = os.listdir(doc_path)
    for i in arr:
        if i.endswith(".txt"):
            
            index_file.update({i:k})
            doc_index.update({k:i})
            k=k+1
            ## take text from number of documents
            fob=open(doc_path+"/"+i,'r')
            txt=fob.read()
            #print(txt)
            fob.close()

            ########################## calling clean function in data_clean.py ############################
            after_stemming = dc.clean(txt)

            for word in after_stemming:
                if word in index_word:
                    #print("yes has key")
                    matrix[index_file[i]][index_word[word]] +=1
                    
                else:
                    # print("no has no key")  
                    index_word.update({word:j})
                    j=j+1
                    
                    if index_file[i]==0 and index_word[word]==0:
                        matrix[index_file[i]][index_word[word]]=1
                        #print(f"$$$$$$ if $$$$$ {matrix}")
                    else:
                        for rows in matrix:
                            rows.extend([0]*1)
                        matrix[index_file[i]][index_word[word]]=1

    
    print("____________________document term matrix-- DTM__________________________")
    print("")
    for ma in matrix:
        print(ma)

    print("")
    print("___________________tfidf - (Term Frequency_inverse document frequency)___")

    no_files=len(index_file)
    col_matrix=len(index_word)

    ###### calling tfdf function in pgm_operations.py
    tfidf_matrix = pgm.tfidf(no_files,col_matrix,matrix)

    ############## printing tf_idf matrix ########################################## 
    print("")        
    for tfidf in tfidf_matrix:
        print(tfidf)
        print("")  

    ############### usind pickle to store tf_idf matrix save permenently in file ########
    io.tfidf_write(tfidf_matrix,index_file,index_word,doc_index,doc_path)
