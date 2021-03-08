# coding: utf-8

import pandas as pd
import random as rd
import os

def generatedTitle():
    
    kanji_file_name = 'data/public/sheena/kanji.csv'
    katakana_file_name = 'data/public/sheena/katakana.csv'
    
    if (os.path.exists(kanji_file_name) and os.path.exists(katakana_file_name)):
        
        kanji_data = pd.read_csv(kanji_file_name, encoding='Shift-JIS')
        katakana_data = pd.read_csv(katakana_file_name, encoding='Shift-JIS')

        kanjis = []
        katakanas = []
        
        kanjis = kanji_data['kanji']
        katakanas = katakana_data['katakana']
        
        if (len(kanjis) > 0 and len(katakanas) > 0):
            
            selected_kanji = ""
            selected_katakana = ""
            
            selected_kanji = rd.choice(kanjis)
            selected_katakana = rd.choice(katakanas)
            
            if (len(selected_kanji) > 0 and len(selected_katakana)):
                
                return selected_kanji + selected_katakana
    
    return ""

def message():
    
    title = generatedTitle()
    
    if (len(title) > 0):
    
        result = title
        result = result + " #椎名林檎"
        result = result + " #新譜"
        result = result + " #タイトル予想"
    
        return result
    
    return ""
