#coding: utf-8

import pandas as pd
import random as rd
import os

def data():
    
    file_name = 'data/public/english/englishvocabulary.csv'
    
    if (os.path.exists(file_name)):
    
        items = pd.read_csv(file_name,encoding="Shift-JIS")

        texts = []
        levels = []

        texts = items['text']
        levels = items['level']
        
        number_of_texts = len(texts)
        
        if (number_of_texts > 0):
            
            if (number_of_texts == len(levels)):

                last_index = number_of_texts - 1
                
                selected_text = ""
                selected_level = ""
                
                if (last_index == 0):
                    
                    selected_text = texts[0]
                    selected_level = levels[0]
                
                else:
    
                    selected_index = rd.randint(0, last_index)
    
                    selected_text = texts[selected_index]
                    selected_level = levels[selected_index]
    
                return [selected_text, selected_level]
    
    return []

def message():
    
    d = data()
    
    if (len(d) == 2):
    
        text = d[0]
        level = d[1]
    
        message = text
        message = message + " "
        message = message + " #英英英単語"
        message = message + " #"
        message = message + level
        
        return message
    
    return ""
