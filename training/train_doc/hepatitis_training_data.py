#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:09:25 2018

@author: justine
"""

import network as nw
#import scikit_learn as sl

question= [["what is hepatitis?"],["what are the symptoms of hepatitis?"],["what is acute hepatitis?"],["what causes hepatitis?"],["what are the other causes of hepatitis?"],["what are the different types of hepatitis?"],["does hepatitis a sexually transmitted diseases?"],["how hepatitis c is spread?"]
,["hepatitis d is infect by what?"],["is there medication available for hepatitis?"],["is there any specific treatment for hepatitis nash?"],["is there liver transplantation an option to cure hepatitis?"]]
selected_sentences_list= [["hepatitis is inflammation of the liver tissue.","hepatitis may be temporary (acute) or long term (chronic) depending on whether it lasts for less than or more than six months."]
                         ,["some people have no symptoms whereas others develop yellow discoloration of the skin and whites of the eyes, poor appetite, vomiting, tiredness, abdominal pain, or diarrhea.","hepatitis is inflammation of the liver tissue."]
                         ,["acute hepatitis can sometimes resolve on its own, progress to its, or rarely result in acute liver failure.","hepatitis may be temporary (acute) or long term (chronic) depending on whether it lasts for less than or more than six months."]
                         ,["the most common cause worldwide is viruses.","other causes of hepatitis include heavy alcohol use, certain medications, toxins, other infections, autoimmune diseases, and non-alcoholic steatohepatitis (nash)."]
                         ,["other causes of hepatitis include heavy alcohol use, certain medications, toxins, other infections, autoimmune diseases, and non-alcoholic steatohepatitis (nash).","hepatitis is inflammation of the liver tissue."]
                         ,["there are five main types of viral hepatitis: type a, b, c, d, and e.","hepatitis is inflammation of the liver tissue."]
                         ,["hepatitis b is mainly sexually transmitted, but may also be passed from mother to baby during pregnancy or childbirth.","other causes of hepatitis include heavy alcohol use, certain medications, toxins, other infections, autoimmune diseases, and non-alcoholic steatohepatitis (nash)."]
                         ,["both hepatitis b and c are commonly spread through infected blood such as may occur during needle sharing by intravenous drug users.","there are five main types of viral hepatitis: type a, b, c, d, and e."]
                         ,["hepatitis d can only infect people already infected with b .","other causes of hepatitis include heavy alcohol use, certain medications, toxins, other infections, autoimmune diseases, and non-alcoholic steatohepatitis (nash)."]
                         ,["medicines may be used to treat chronic cases of viral hepatitis.","other causes of hepatitis include heavy alcohol use, certain medications, toxins, other infections, autoimmune diseases, and non-alcoholic steatohepatitis (nash)."]
                         ,["there is no specific treatment for nash; however, a healthy lifestyle, including physical activity, a healthy diet, and weight loss, is important.","other causes of hepatitis include heavy alcohol use, certain medications, toxins, other infections, autoimmune diseases, and non-alcoholic steatohepatitis (nash)."]
                         ,["a liver transplant may also be an option in certain cases.","over time the chronic form may progress to scarring of the liver, liver failure, or liver cancer."]]

for i in range (0, len(question)):
    
    array=nw.question_answer_nurel_network(question[i],selected_sentences_list[i])
#answer= nw.question_answer_nurel_network(question,selected_sentences_list)
#print(answer)
print("array= " +str(array))

#net=sl.learn(array)
#sl.save_perceptron(net)

