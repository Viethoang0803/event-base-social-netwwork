import csv
list_des = []
with open(r"D:\code_bigdata\filter3_drop-greater_100_attendees\description_filter3.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_des.append(row)
        
sorted_data = sorted(list_des, key=lambda x: x[1])

#loại bỏ word trùng trong 1 list
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


#ghép mô tả theo nhóm
list_doc = []
list_index=[]
subdoc = []
index_doc = 0
    
 
t=''
for i in range(len(sorted_data)):
    if(i==len(sorted_data)-1):
        list_index.append([index_doc,i])
        t = t+ ' '+ sorted_data[i][3]        
        list_doc.append(t)
        break
    if(sorted_data[i][1] == sorted_data[i+1][1]):
        list_index.append([index_doc,i])
        t = t+ ' '+ sorted_data[i][3]
    else:
        list_index.append([index_doc,i] )
        t = t+ ' '+ sorted_data[i][3]
        list_doc.append(t)
        t=''
        index_doc = index_doc+1
        
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re
nltk.download('stopwords')  
from nltk.corpus import stopwords   
nltk.download('words')
from nltk.corpus import words
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()


stop_words =set(stopwords.words('english'))        
english_words = set(words.words())



list_doc_nltk = []
for i in range(len(list_doc)):
    sentence = list_doc[i]
    list_doc[i] = re.sub(r'[^\x00-\x7F]+', ' ', sentence)

for i in range(len(list_doc)):
    list_doc[i] =set(word_tokenize(list_doc[i]))

for i in range(len(list_doc)):    
    list_doc[i] = [stemmer.stem(word) for word in list_doc[i]]

for i in range(len(list_doc)):
    list_doc[i] = [word.lower() for word in list_doc[i]]

for i in range(len(list_doc)):    
    list_doc[i] = [word for word in list_doc[i] if word not in stop_words]

for i in range(len(list_doc)):    
    list_doc[i] = [word for word in list_doc[i] if word in english_words]

for i in range(len(list_doc)):
    list_doc[i] = remove_duplicates(list_doc[i])
 


#xử lý description của từng event một
list_text_event = []
for i in sorted_data:
    list_text_event.append(i[3]) 

#xóa ký tự đặc biệt
for i in range(len(sorted_data)):
    list_text_event[i] = re.sub(r'[^\x00-\x7F]+', ' ', list_text_event[i])     

#tách các chữ cái
for i in range(len(sorted_data)):
    list_text_event[i] =set(word_tokenize(list_text_event[i]))
    
#bỏ đuôi s,es,... quy về dạng thường của word
for i in range(len(sorted_data)):    
    list_text_event[i] = [stemmer.stem(word) for word in list_text_event[i]]

#viết thường tất cả các word
for i in range(len(sorted_data)):
    list_text_event[i] = [word.lower() for word in list_text_event[i]]

#loại bỏ stop word
for i in range(len(sorted_data)):   
    list_text_event[i] = [word for word in list_text_event[i] if word not in stop_words]

#lấy những từ English word
for i in range(len(sorted_data)):
    list_text_event[i] = [word for word in list_text_event[i] if word in english_words]
 
#loại bỏ những từ trùng lặp
for i in range(len(sorted_data)):
    list_text_event[i] = remove_duplicates(list_text_event[i])
 
    

#tính độ tương quan
    
#khai báo thư viện
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

'''
#test
x=30050
a_vals = Counter(list_text_event[x])
b_vals = Counter(list_doc[list_index[x][0]])

# convert to word-vectors
words  = list(a_vals.keys() | b_vals.keys())
a_vect = [a_vals.get(word, 0) for word in words]       
b_vect = [b_vals.get(word, 0) for word in words]        

c= cosine_similarity([a_vect], [b_vect])[0][0]
print(c)

print(len(list_text_event[x]))
print(list_doc[list_index[x][0]])
print(sorted_data[x])
'''

#tính độ tương quan

list_similarity = []
for i in range(len(list_index)):
    if(len(list_text_event[i]) !=0):
        # count word occurrences
        a_vals = Counter(list_text_event[i])
        b_vals = Counter(list_doc[list_index[i][0]])
    
        # convert to word-vectors
        words  = list(a_vals.keys() | b_vals.keys())
        a_vect = [a_vals.get(word, 0) for word in words]       
        b_vect = [b_vals.get(word, 0) for word in words] 
        
        c= cosine_similarity([a_vect], [b_vect])[0][0]
        list_similarity.append(c)
    else:
        list_similarity.append(0)




for i in range(len(list_index)):
    c=round(list_similarity[i], 5)
    sorted_data[i].insert(3,c)

#thay bằng des đã xử lý      
for i in range(len(sorted_data)):
    sorted_data[i].pop(4)
    result_string = ' '.join(list_text_event[i])
    sorted_data[i].append(result_string)
#xóa id
for i in range(len(sorted_data)):
    sorted_data[i].pop(0)

name = ['group_id','event_id','similar','description']
sorted_data.insert(0,name)

with open(r"D:\code_bigdata\process2_des_NLTK\process2_des_NLTK.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(sorted_data)
                



