import pandas as pd
import random as rd
import os

def data():
    
    file_name = 'labs/data/public/comic/zemmyon.csv'
    
    if (os.path.exists(file_name)):
    
        items = pd.read_csv(file_name,encoding="utf-8")

        words = []
        urls = []

        words =  items['word']
        urls = items['url']
        
        if (len(words) > 0 and len(urls) > 0):
            
            if (len(words) == len(urls)):

                number_of_words = len(words)
                last_index = number_of_words - 1
                
                selected_word = ""
                selected_url = ""
                
                if (last_index == 0):
                    
                    selected_word = words[0]
                    selected_url = urls[0]
                
                else:
    
                    selected_index = rd.randint(0, last_index)
    
                    selected_word = words[selected_index]
                    selected_url = urls[selected_index]
    
                return [selected_word, selected_url]
    
    return []

def message():
    
    cd = data()
    
    if (len(cd) == 2):
    
        word = cd[0]
        url = cd[1]
    
        message = word
        message = message + " "
        message = message + " #全みょん"
        message = message + " #おほしんたろう"
        message = message + " "
        message = message + url
        
        return message
    
    return ""
