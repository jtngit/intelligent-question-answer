#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:09:25 2018

@author: justine
"""

import network as nw
#import scikit_learn as sl

question= [["what is a stroke?"],["what are the types of strokes present?"],["what are the signs and symptoms of strokes?"],["when dose the sighs and symptoms of stroke often appear?"],["what if symptoms of stroke last less than one or more hour?"],["to what a hemorrhagic stroke may also associated with?"],["can the symptoms of strokes be permanent?"],["what are the long-term complications of stroke?"]
,["what is the risk factor for stroke?"],["an ischemic stroke is typically caused by what?"],["a hemorrhagic stroke is caused by what?"],["bleeding during stroke occur due to what?"],["the stroke diagnosis is typically based on what?"],["what are the other tests for stroke?"],["what causes the similar symptoms to stroke?"],["how to prevent stroke?"],["does a stroke require emergency care?"],["what if an ischemic stroke is detected?"]
,["what is rehabilitation for stroke?"],["approximately how many people have stroke?"],["does people recover from stroke?"],["does people death in a stroke?"]]
selected_sentences_list= [["a stroke is a medical condition in which poor blood flow to the brain results in cell death.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["there are two main types of stroke: ischemic, due to lack of blood flow, and hemorrhagic, due to bleeding, they result in part of the brain not functioning properly.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["signs and symptoms of a stroke may include an inability to move or feel on one side of the body, problems understanding or speaking, dizziness, or loss of vision to one side.","sighs and symptoms often appear soon after the stroke has occurred."]
                         ,["sighs and symptoms often appear soon after the stroke has occurred.","signs and symptoms of a stroke may include an inability to move or feel on one side of the body, problems understanding or speaking, dizziness, or loss of vision to one side."]
                         ,["if symptoms last less than one or two hours it is known as a transient ischemic attack (tia) or mini-stroke.","signs and symptoms of a stroke may include an inability to move or feel on one side of the body, problems understanding or speaking, dizziness, or loss of vision to one side."]
                         ,["a hemorrhagic stroke may also be associated with a severe headache.","there are two main types of stroke: ischemic, due to lack of blood flow, and hemorrhagic, due to bleeding, they result in part of the brain not functioning properly."]
                         ,["the symptoms of a stroke can be permanent.","signs and symptoms of a stroke may include an inability to move or feel on one side of the body, problems understanding or speaking, dizziness, or loss of vision to one side."]
                         ,["long-term complications may include pneumonia or loss of bladder control.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["the main risk factor for stroke is high blood pressure and other risk factors include tobacco smoking, obesity, high blood cholesterol, diabetes mellitus, a previous tia, and atrial fibrillation.","stroke prevention includes decreasing risk factors, as well as possibly aspirin, statins, surgery to open up the arteries to the brain in those with problematic narrowing, and warfarin in those with atrial fibrillation."]
                         ,["an ischemic stroke is typically caused by blockage of a blood vessel, though there are also less common causes.","in 2015, stroke was the second most frequent cause of death after coronary artery disease, accounting for 6.3 million deaths (11% of the total), about 3.0 million deaths resulted from ischemic while 3.3 million deaths resulted from hemorrhagic."]
                         ,["a hemorrhagic stroke is caused by either bleeding directly into the brain or into the space between the brain's membranes.","an ischemic stroke is typically caused by blockage of a blood vessel, though there are also less common causes."]
                         ,["bleeding may occur due to a ruptured brain aneurysm.","there are two main types of stroke: ischemic, due to lack of blood flow, and hemorrhagic, due to bleeding, they result in part of the brain not functioning properly."]
                         ,["diagnosis is typically based on a physical exam and supported by medical imaging such as a ct scan or mri scan.","an ischemic stroke is typically caused by blockage of a blood vessel, though there are also less common causes."]
                         ,["other tests such as an electrocardiogram (ecg) and blood tests are done to determine risk factors and rule out other possible causes.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["low blood sugar may cause similar symptoms.","an ischemic stroke is typically caused by blockage of a blood vessel, though there are also less common causes."]
                         ,["stroke prevention includes decreasing risk factors, as well as possibly aspirin, statins, surgery to open up the arteries to the brain in those with problematic narrowing, and warfarin in those with atrial fibrillation.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["a stroke or tia often requires emergency care.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["an ischemic stroke, if detected within three to four and half hours, may be treatable with a medication that can break down the clot.","there are two main types of stroke: ischemic, due to lack of blood flow, and hemorrhagic, due to bleeding, they result in part of the brain not functioning properly."]
                         ,["treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world.","a stroke is a medical condition in which poor blood flow to the brain results in cell death."]
                         ,["in 2013 approximately 6.9 million people had an ischemic stroke and 3.4 million people had a hemorrhagic stroke.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["in 2015 there were about 42.4 million people who had previously had a stroke and were still alive.","treatment to try to recover lost function is called stroke rehabilitation and ideally takes place in a stroke unit; however, these are not available in much of the world."]
                         ,["in 2015, stroke was the second most frequent cause of death after coronary artery disease, accounting for 6.3 million deaths (11% of the total), about 3.0 million deaths resulted from ischemic while 3.3 million deaths resulted from hemorrhagic.","in 2013 approximately 6.9 million people had an ischemic stroke and 3.4 million people had a hemorrhagic stroke."]]
                         

for i in range (0, len(question)):
    
    array=nw.question_answer_nurel_network(question[i],selected_sentences_list[i])
#answer= nw.question_answer_nurel_network(question,selected_sentences_list)
#print(answer)
print("array= " +str(array))

#net=sl.learn(array)
#sl.save_perceptron(net)

