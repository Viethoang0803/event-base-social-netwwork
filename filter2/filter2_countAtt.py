import csv

list_attendees = []

#read file attendees in filter 1
with open(r"D:\code_bigdata\filter1\attendees_filter1.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if(len(row)>9):
            list_attendees.append(row)

list_person_id = []
list_count= []

#đếm số người có tham gia trong sự kiện(yes thì đếm)
for i in range(len(list_attendees)):
    count = 0
    for j in range(len(list_attendees[i])-5):
        list_attendees[i][j+5] = list_attendees[i][j+5].split("_")
        if( list_attendees[i][j+5][2][0] == "y"):
            count=count+1
            list_person_id.append(list_attendees[i][j+5][0])
    list_count.append(count)

#chèn thêm một cột số người thực tế tham gia
for i in range(len(list_attendees)):
    list_attendees[i].insert(5, list_count[i])
    
#ghi lại file attenndees mới        
with open(r"D:\code_bigdata\filter2\atendees_filter2.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_attendees)


#set id của attendees
list_attendees_idE = []
for i in list_attendees:
    list_attendees_idE.append(i[3])
set_att_idE = set(list_attendees_idE)


print(list_attendees_idE[0])

