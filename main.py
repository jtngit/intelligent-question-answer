import first as k
import question as que


doc_path='/doc'
k.runstart(doc_path)
k.doc_clean_and_tfidf(doc_path)

i='y'
while (i == 'y'):

    selected_sentences= que.questions()
    for sen in selected_sentences:
        print(sen)
    print("*******************************************************\n\n")
    print("Answer : {}" .format(selected_sentences[0]))
    print("*******************************************************\n\n")
    i = input("press 'y' continue \n press 'n' exit-\n")
