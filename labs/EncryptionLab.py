# coding: utf-8

import numpy as np
import random as rd
import pandas as pd
import os

def data():
    
    file_name = 'data/private/future/keywords.csv'
    
    if (os.path.exists(file_name)):
    
        items = pd.read_csv(file_name,encoding="utf-8")
        keywords = items['keyword']
        
        if (len(keywords) > 0):
            return keywords.values.tolist()
    
    return []

def selected_keyword():
    
    keywords = data()
    number_of_keywords = len(keywords)
    
    if (number_of_keywords > 0):
            
        last_index = number_of_keywords - 1
                
        selected_keyword = ""
                
        if (last_index == 0):
            selected_keyword = keywords[0]
                
        else:
            selected_index = rd.randint(0, last_index)
            selected_keyword = keywords[selected_index]
    
        return selected_keyword
    
    return ""

def created_key():
    
    list_key = []
    list_sign = [1,-1]
    
    for key in range(1,7):
        list_key.append(key*rd.choice(list_sign))
        
    return list_key

def encrypted_alphabet(alphabet, keys):

    mat_alphabet = np.array(alphabet)
    mat_alphabet = mat_alphabet.reshape(6,6)
    tr_mat_alphabet = mat_alphabet.T
    
    for key in keys:
        
        index = abs(key) - 1
    
        if key < 0:
            row_letters = tr_mat_alphabet[index]
            row_letters = row_letters[::-1]
            tr_mat_alphabet[index] = row_letters
        
    en_alphabet = tr_mat_alphabet.ravel()
    
    return en_alphabet.tolist()

def decrypted_message(en_message, en_alphabet):
    
    message = ""
    
    raw_alphabet = [
                        "0","1","2","3","4","5",
                        "6","7","8","9","A","B",
                        "C","D","E","F","G","H",
                        "I","J","K","L","M","N",
                        "O","P","Q","R","S","T",
                        "U","V","W","X","Y","Z"
                    ]
    
    for letter in en_message:
        
        try:
            index = en_alphabet.index(letter)
            message += raw_alphabet[index]
            
        except ValueError as error:
            message += letter
            
    return message

def encrypted_message(message):
    
    raw_message = message.upper()
    en_message = ""
    
    raw_alphabet = [
                        "0","1","2","3","4","5",
                        "6","7","8","9","A","B",
                        "C","D","E","F","G","H",
                        "I","J","K","L","M","N",
                        "O","P","Q","R","S","T",
                        "U","V","W","X","Y","Z"
                    ]
    
    keys = created_key()
    en_alphabet = encrypted_alphabet(raw_alphabet, keys)
    
    for letter in raw_message:
        
        try:
            index = raw_alphabet.index(letter)
            en_message += en_alphabet[index]
            
        except ValueError as error:
            en_message += letter
            
    if (isSuccessInEncryption(en_message, en_alphabet)):
        return en_message
            
    return ""

def isSuccessInEncryption(en_message, en_alphabet):
    
    de_message = decrypted_message(en_message, en_alphabet)
    keywords = data()
    
    if (len(keywords) > 0):
        return (de_message in keywords)
    
    return False
    

def message():
    
    raw_message = selected_keyword()
    en_message = encrypted_message(raw_message)
    
    if (len(en_message) > 0):
        
        en_message = en_message + " #cryptogram"
        en_message = en_message + " #暗号文"
        
        return en_message
    
    return ""
