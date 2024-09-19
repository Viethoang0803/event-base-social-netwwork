import csv
import pandas as pd
import numpy as np

list_info_eID = []

with open(r"D:\code_bigdata\filter1\info_file.csv",'r', encoding = 'iso-8859-1')as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    list_info_eID.append(row[3])


list_info_eID = list_info_eID[1:]
set_info = set(list_info_eID)


#lấy file description
list_des = []
with open ("D:/7.reseach/NewYork_event_description2012_2020.txt", 'r', encoding = 'iso-8859-1')as file:
    for line in file:
            process_line = line.strip()
            process1 = process_line.split('\t')
            if(process1[2] in set_info): 
                list_des.append(process1)
with open(r"D:\code_bigdata\filter1\description_filter1.csv","w",encoding="iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_des)           
            
    
    
    
list_venue = []
with open (r"D:\7.reseach\newyork_event_venue2012_2020.txt", 'r', encoding = 'iso-8859-1')as file:
    for line in file:
            process_line = line.strip()
            process1 = process_line.split('\t')
            if(process1[2] in set_info): 
                list_venue.append(process1)
with open(r"D:\code_bigdata\filter1\venue_filter1.csv","w",encoding="iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_venue)
    
    
    
    
    
    
    
list_att = []
with open (r"D:\7.reseach\newyork_event_attendees2012_2020.txt", 'r', encoding = 'iso-8859-1')as file:
    for line in file:
            process_line = line.strip()
            process1 = process_line.split('\t')
            if(process1[3] in set_info): 
                list_att.append(process1)
with open(r"D:\code_bigdata\filter1\attendees_filter1.csv","w",encoding="iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_att)
        
    
        

