import csv
list_attendees = []

#read file attendees in filter 2
with open(r"D:\code_bigdata\filter2\atendees_filter2.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if int(row[5])< 101:
            list_attendees.append(row)
            
set_att = set([x[3] for x in list_attendees])
#filter venue by attendees(1, trùng even_id với att thì giữ lại,2 mỗi even id trong list chỉ được xuất hiện 1 lần )
list_venue = []
set_eid_venue = set()
with open(r"D:\code_bigdata\filter1\venue_filter1.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if(row[2] in set_att and row[2] not in set_eid_venue):
            list_venue.append(row)
            set_eid_venue.add(row[2])

                
    
#filter venue by des(1, trùng even_id với att thì giữ lại,2 mỗi even id trong list chỉ được xuất hiện 1 lần )
list_des = []
set_eid_des = set()
with open(r"D:\code_bigdata\filter1\description_filter1.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if(row[2] in set_att and row[2] not in set_eid_des and row[2] in set_eid_venue and len(row)>3):
            list_des.append(row)
            set_eid_des.add(row[2])


#filter venue by info(1, trùng even_id với att thì giữ lại,2 mỗi even id trong list chỉ được xuất hiện 1 lần )
list_info = []
set_eid_info = set()
with open(r"D:\code_bigdata\filter1\info_file.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if(row[3] in set_att and row[3] not in set_eid_info and row[3] in set_eid_venue and row[3] in set_eid_des):
            list_info.append(row)
            set_eid_info.add(row[3])
            

#loc nhung evenid khong co trong nhung file khac(des and info da loc)
list_attendees1=[]
list_venue1=[]
set_test = set()

for i in list_attendees:
    if i[3] in set_eid_info and i[3] not in set_test:
        list_attendees1.append(i)
        set_test.add(i[3])
set_test = set()
for i in list_venue:
    if i[2] in set_eid_info:
        list_venue1.append(i)
        set_test.add(i[3])
                
#export file att
with open(r"D:\code_bigdata\filter3_drop-greater_100_attendees\attendees_filter3.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_attendees1)            
            
#export file venue
with open(r"D:\code_bigdata\filter3_drop-greater_100_attendees\venue_filter3.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_venue1)            
            
#export file des
with open(r"D:\code_bigdata\filter3_drop-greater_100_attendees\description_filter3.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_des)
            
#export file info
with open(r"D:\code_bigdata\filter3_drop-greater_100_attendees\infomation_filter3.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_info)
            

            