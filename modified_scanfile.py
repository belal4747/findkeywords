from datetime import datetime
import re
import csv
import string
from flashtext import KeywordProcessor
startTime = datetime.now()
keyword_processor = KeywordProcessor()


def find_sentence(text,keyword):
    line_end_chars = "!", "?", "."
    regexPattern = '|'.join(map(re.escape, line_end_chars))
    line_list = re.split(regexPattern, text)
    for line in line_list:
        if keyword in line:          
           line= (" " + line)
           return line     


dict_of_war=['bomb','Bomb','ISIS','destruction','kill','death','violence','Conflict', 'political','tensions']
dict_of_terrorism=['korea','interpol','terrorism', 'terror', 'attacks','nuclear','bomb','threats','conflicts','war','tensions', 'political']
dict_of_disease=['disease','epidemic','pandemic','outbreak']
dict_of_disaster=['disaster','natural','calamity','natural','earthquake','flood','forest','fires','tsunami','draught','draughts','flood','cyclone','hurricane','tornadoes','volcano','eruption','thunder','volcanoes','Limnic','landslide','typhoon','cyclone','Blizzard','Tornado']
dict_of_recession=['recession','depression']
dict_of_layoff=['layoff','Layoffs','firing','furloughed','Furloughed','furloughs','Furloughs','Salary Cuts','salary cuts', 'severance','paycut','paycheck','downsizing','downsize']
dict_of_inflation=['inflation' ]
dict_of_deflation=['deflation']
dict_of_Interest=['Interest','Rates', 'Repo','MCLR','Rate','lending' 'rate','basis','points']
dict_of_gdp=['GDP','gross','domestic','product','yield']
dict_of_gold=['gold','bullion']
dict_of_unemployment=['unemployment','Unemployment']
dict_of_crude=['Crude','crude','Oil','oil','Barrels','barrels','Opec','opec','OPEC']
dict_of_vix=['vix','volatility','cboe']
dict_of_central=['policy']
dict_of_parameters=['inflation','deflation','Interest', 'Repo','MCLR','lending','lending rate','basis points','GDP','gross','domestic','product''yield','gold','bullion','crude','oil','barrels','opec','vix','volatility','cboe']
dict_of_increase=['Increase','increase','spike','rise','shot up','hike','soaring']
dict_of_decrease=['decrease','Decrease','collapse','decline','Decline','collapsing']

with open('csvout0601.csv') as searchfile:
    text = searchfile.read()
    

    for keyword in dict_of_unemployment:
        text_with_keywords=find_sentence(text,keyword)
        print(text_with_keywords)
        if text_with_keywords:
            for param in dict_of_increase:
                if find_sentence(text_with_keywords,param):
                    print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
            for param in dict_of_decrease:
                if find_sentence(text_with_keywords,param):
                    print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")

    
    for keyword in dict_of_inflation:
        text_with_keywords=find_sentence(text,keyword)
        print(text_with_keywords)
        if text_with_keywords:
           for param in dict_of_increase:
               if find_sentence(text_with_keywords,param):
                   print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
           for param in dict_of_decrease:
                if find_sentence(text_with_keywords,param):
                    print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")

        for keyword in dict_of_deflation:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               for param in dict_of_increase:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
               for param in dict_of_decrease:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")
            
        for keyword in dict_of_Interest:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               for param in dict_of_increase:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
               for param in dict_of_decrease:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")
        
        for keyword in dict_of_gdp:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               for param in dict_of_increase:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
               for param in dict_of_decrease:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")
        
        for keyword in dict_of_gold:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               for param in dict_of_increase:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
               for param in dict_of_decrease:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")

        for keyword in dict_of_crude:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               for param in dict_of_increase:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
               for param in dict_of_decrease:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")

        for keyword in dict_of_vix:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               for param in dict_of_increase:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is increasing")
               for param in dict_of_decrease:
                    if find_sentence(text_with_keywords,param):
                       print ("Keywords related to the term" + " " + keyword + " " + "found in the news article and trend is decreasing")
            

        for keyword in dict_of_war:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               print ("Keywords related to the term" + " " + keyword + " " + "found in the news article which has relevance to keyword war")

        for keyword in dict_of_terrorism:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               print ("Keywords related to the term" + " " + keyword + " " + "found in the news article which has relevance to keyword terrorism")

        for keyword in dict_of_disease:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               print ("Keywords related to the term" + " " + keyword + " " + "found in the news article which has relevance to keyword disease")


        for keyword in dict_of_disaster:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               print ("Keywords related to the term" + " " + keyword + " " + "found in the news article which has relevance to keyword Natural Calamity or Natural Disaster")

        for keyword in dict_of_recession:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               print ("Keywords related to the term" + " " + keyword + " " + "found in the news article which has relevance to keyword Depression")

        for keyword in dict_of_layoff:
            text_with_keywords=find_sentence(text,keyword)
            print(text_with_keywords)
            if text_with_keywords:
               print ("Keywords related to the term" + " " + keyword + " " + "found in the news article which has relevance to keyword Layoff")