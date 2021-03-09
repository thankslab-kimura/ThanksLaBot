# coding: utf-8

import numpy as np
import random as rd

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
            
    print(decrypted_message(en_message, en_alphabet))
            
    return en_message
