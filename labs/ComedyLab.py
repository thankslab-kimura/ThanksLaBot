# coding: utf-8

import pandas as pd
import random as rd
import os

def data():
    
    file_name = 'labs/data/public/youtube/comedy.csv'
    
    if (os.path.exists(file_name)):
    
        items = pd.read_csv(file_name,encoding="utf-8")

        channels = []
        titles = []
        urls = []

        channels =  items['channel']
        titles =  items['title']
        urls = items['url']
        
        if (len(channels) > 0 and len(titles) > 0 and len(urls) > 0):
            
            if (len(channels) == len(titles) and len(titles) == len(urls)):

                number_of_titles = len(titles)
                last_index = number_of_titles - 1
                
                selected_channel = ""
                selected_title = ""
                selected_url = ""
                
                if (last_index == 0):
                    
                    selected_channel = channels[0]
                    selected_title = titles[0]
                    selected_url = urls[0]
                
                else:
    
                    selected_index = rd.randint(0, last_index)
    
                    selected_channel = channels[selected_index]
                    selected_title = titles[selected_index]
                    selected_url = urls[selected_index]
    
                return [selected_channel, selected_title, selected_url]
    
    return []

def message():
    
    d = data()
    
    if (len(d) == 3):
    
        channel = d[0]
        title = d[1]
        url = d[2]
    
        message = channel
        message = message + "『"
        message = message + title
        message = message + "』"
        message = message + " #YouTube"
        message = message + " #Comedy"
        message = message + " "
        message = message + url
        
        return message
    
    return ""
