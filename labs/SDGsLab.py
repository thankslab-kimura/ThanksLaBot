# coding: utf-8

import pandas as pd
import random as rd
import os

def data():
    
    file_name = 'labs/data/public/sdgs/targets.csv'
    
    if (os.path.exists(file_name)):
    
        items = pd.read_csv(file_name,encoding="utf-8")

        indices = []
        targets = []
        
        indices = items['index']
        targets =  items['target']
        
        if (len(targets) > 0):
            
            number_of_targets = len(targets)
            
            if (number_of_targets == len(indices)):
            
                last_index = number_of_targets - 1
                
                selected_index = ""
                selected_target = ""
                
                if (last_index == 0):
                    
                    selected_index = indices[0]
                    selected_targets = targets[0]
                
                else:
    
                    i = rd.randint(0, last_index)
        
                    selected_index = indices[i]
                    selected_target = targets[i]
            
            if (len(selected_index) and len(selected_target) > 0):
                return [selected_index, selected_target]
    
    return []

def message():
    
    d = data()
    
    if (len(d) == 2):
        
        index = ""
        target = ""
        
        index = d[0]
        target = d[1]
        
        if (len(index) > 0 and len(target) > 0):
        
            message = index + " : "
            message = message + target
            message = message + " "
            message = message + " #SDGs"
            message = message + " #国連"
            message = message + " #持続可能な開発目標"
            message = message + " #17の目標"
            message = message + " #169のターゲット"
        
            return message
    
    return ""
