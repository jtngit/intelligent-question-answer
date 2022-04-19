import math

def tfidf(no_files,col_matrix,matrix):

    ######### creating matrix with all zeros ##########################################
    tfidf_matrix=[]
    for rw in range (0,no_files):
        tfidf_matrix.append([0]*col_matrix)
        
    #for idf in tfidf_matrix:
        # print(idf)
        
    #print("##########################################################################")

    for h in range(0,no_files):
        for f in range(0,col_matrix):
            # print(sum(matrix[h]))
            ###### no of times word in the doc / total no words in the doc ##########
            tf = float(matrix[h][f]) / float(sum(matrix[h]))
            #print("__________ printing tf__________________")   
            #print(tf)
            ############## counting no documents that contains that word ###############
            count_doc=0
            for s in range(0,no_files):
                if matrix[s][f] != 0:
                    count_doc += 1
            #print(count_doc)
            ########### no of doc / no doc contains that word #######################
            idf = math.log(float(no_files)/float(count_doc))
            #print(idf)
            tfidf_matrix[h][f] = tf*idf
    
    return tfidf_matrix
    