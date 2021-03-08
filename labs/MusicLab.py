# coding: utf-8

import pandas as pd
import random as rd
import os

def data():
    
    file_name = 'data/public/youtube/music.csv'
    
    if (os.path.exists(file_name)):
    
        items = pd.read_csv(file_name,encoding="Shift-JIS")

        artists = []
        titles = []
        urls = []

        artists =  items['artist']
        titles =  items['title']
        urls = items['url']
        
        if (len(artists) > 0 and len(titles) > 0 and len(urls) > 0):
            
            if (len(artists) == len(titles) and len(artists) == len(urls)):

                number_of_titles = len(titles)
                last_index = number_of_titles - 1
                
                selected_artist = ""
                selected_title = ""
                selected_url = ""
                
                if (last_index == 0):
                    
                    selected_artist = artists[0]
                    selected_title = titles[0]
                    selected_url = urls[0]
                
                else:
    
                    selected_index = rd.randint(0, last_index)
    
                    selected_artist = artists[selected_index]
                    selected_title = titles[selected_index]
                    selected_url = urls[selected_index]
    
                return [selected_artist, selected_title, selected_url]
    
    return []

def message():
    
    d = data()
    
    if (len(d) == 3):
    
        artist = d[0]
        title = d[1]
        url = d[2]
    
        message = artist
        message = message + " - "
        message = message + title
        message = message + " "
        message = message + " #YouTube"
        message = message + " #MusicVideo"
        message = message + " "
        message = message + url
        
        return message
    
    return ""
