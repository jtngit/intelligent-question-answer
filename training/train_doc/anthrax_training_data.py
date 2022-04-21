
import network as nw

question= [["what is anthrax?"],["how anthrax is occurred?"],["when symptoms of anthrax begins in?"],["what are the symptoms of anthrax?"],["how anthrax is spread?"],["what are the risk factors of anthrax?"],["how could anthrax diagnosis be confirmed?"],["anthrax vaccination is recommended for whome?"]
,["how anthrax infection can be prevented?"],["what if anthrax infection occurred?"],["which drug is recommended for those with widespread infection of anthrax?"],["where is this anthrax disease commonly occurred?"],["how many anthrax infection cases occurs globally?"],["what is the risk of skin anthrax without treatment?"]
,["how much is the risk for intestinal infection of anthrax?"],["how many people where killed by anthrax?"],["how anthrax infections spread in animals?"]]
selected_sentences_list= [["anthrax is an infection caused by the bacterium bacillus anthracis.","the symptoms of anthrax skin form presents with a small blister with surrounding swelling that often turns into a painless ulcer with a black center ."]
                         ,["it can occur in four forms: skin, lungs, intestinal, and injection.","immunizing animals against anthrax is recommended in areas where previous infections have occurred"]
                         ,["symptoms begin between one day and two months after the infection is contracted.","the symptoms of anthrax skin form presents with a small blister with surrounding swelling that often turns into a painless ulcer with a black center ."]
                         ,["the symptoms of anthrax skin form presents with a small blister with surrounding swelling that often turns into a painless ulcer with a black center .","anthrax is an infection caused by the bacterium bacillus anthracis."]
                         ,["anthrax is spread by contact with the bacterium's spores, which often appear in infectious animal products.","anthrax is an infection caused by the bacterium bacillus anthracis."]
                         ,["risk factors include people who work with animals or animal products, travelers, postal workers, and military personnel.","anthrax vaccination is recommended for people who are at high risk of infection."]
                         ,["diagnosis can be confirmed based on finding antibodies or the toxin in the blood or by culture of a sample from the infected site.","anthrax is an infection caused by the bacterium bacillus anthracis."]
                         ,["anthrax vaccination is recommended for people who are at high risk of infection.","immunizing animals against anthrax is recommended in areas where previous infections have occurred"]
                         ,["two months of antibiotics such as ciprofloxacin, levofloxacin, and doxycycline after exposure can also prevent infection.","anthrax is an infection caused by the bacterium bacillus anthracis."]
                         ,["if infection occurs treatment is with antibiotics and possibly antitoxin.","immunizing animals against anthrax is recommended in areas where previous infections have occurred"]
                         ,["antitoxin is recommended for those with widespread infection.","immunizing animals against anthrax is recommended in areas where previous infections have occurred"]
                         ,["though a rare disease, human anthrax, when it does occur, is most common in africa and central and southern asia.","immunizing animals against anthrax is recommended in areas where previous infections have occurred"]
                         ,["globally, at least 2,000 cases occur a year with about two cases a year in the united states.","immunizing animals against anthrax is recommended in areas where previous infections have occurred"]
                         ,["without treatment, the risk of death from skin anthrax is 24%.","for intestinal infection, the risk of death is 25 to 75%, while respiratory anthrax has a mortality of 50 to 80%, even with treatment."]
                         ,["for intestinal infection, the risk of death is 25 to 75%, while respiratory anthrax has a mortality of 50 to 80%, even with treatment.","anthrax vaccination is recommended for people who are at high risk of infection."]
                         ,["until the 20th century, anthrax infections killed hundreds of thousands of people and animals each year.","anthrax vaccination is recommended for people who are at high risk of infection."]
                         ,["in plant-eating animals, infection occurs when they eat or breathe in the spores while grazing.","anthrax is spread by contact with the bacterium's spores, which often appear in infectious animal products."]]

for i in range (0, len(question)):
    
    array=nw.question_answer_nurel_network(question[i],selected_sentences_list[i])

