import csv

#read file info in filter4
list_info = []
with open(r"D:\code_bigdata\filter3_drop-greater_100_attendees\infomation_filter3.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_info.append(row)
        
#sắp xếp theo group_id
sorted_data = sorted(list_info, key=lambda x: x[1])
list_mean = []

#tính độ lệch giờ
sum = 0
count=1
mean=0
for i in range(len(sorted_data)):
    if(i==len(sorted_data)-1):
        sum = sum + int(sorted_data[i][10])
        mean = float(sum)/(count+1)
        for i in range(count):
            list_mean.append(mean)
        break   
    elif(sorted_data[i][1] == sorted_data[i+1][1]):
        count = count+1
        sum = sum + int(sorted_data[i][10])
    else:
        sum = sum + int(sorted_data[i][10])
        mean = float(sum) / count
        for i in range(count):
            list_mean.append(mean)
        count =1
        sum =0

dolech = []
for i in range(len(list_info)):
    dolech.append(float(sorted_data[i][10]) - list_mean[i])                                                                     
            
for i in range(len(list_info)):
    sorted_data[i].insert(11, dolech[i])
            
day_to_number = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

list_thu = []

for row in sorted_data:
    day_name = row[12]
    day_number = day_to_number[day_name]
    list_thu.append(day_number)
            
#code tính độ lệch thứ trong tuần
list_mean=[]
sum = 0
count=1
mean=0
for i in range(len(sorted_data)):
    if(i==len(sorted_data)-1):
        sum = sum + int(list_thu[i])
        mean = float(sum)/(count+1)
        for i in range(count):
            list_mean.append(mean)
        break
    elif(sorted_data[i][1] == sorted_data[i+1][1]):
        count = count+1
        sum = sum + int(list_thu[i])
    else:
        sum = sum + int(list_thu[i])
        mean = float(sum) / count
        for i in range(count):
            list_mean.append(mean)
        count = 1
        sum = 0
        
dolech = []
for i in range(len(list_info)):
    dolech.append(float(list_thu[i])- list_mean[i] )


for i in range(len(list_info)):
    sorted_data[i].insert(13, dolech[i])
    
#cột time(lấy s thay vì ms)
for i in range(len(list_info)):
    sorted_data[i][14] = int(int(sorted_data[i][14])/10000)
    
    
with open(r"D:\code_bigdata\process1_cal_infoDev\infomation_process1.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(sorted_data)
            
            
            
            