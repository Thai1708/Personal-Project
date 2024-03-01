import pandas as pd

with open('data_jobsgo.txt', 'r', encoding='utf8') as file:
    data = file.read()

list_data = data.split("html#")
list_data.pop()

for i in range(len(list_data)):
    list_data[i] = list_data[i].replace('\n', '')
    
title_list = []
company_list = []
salary_list = []
location_list = []
date_list = []
cap_list = []
nganh_list = []
kinnghiem_list = []
hinhthuc_list = []
yeucau_list = []
bangcap_list = []
link_list = []

lenght_list = []

for i in range(len(list_data)):
    sub_list = list_data[i].split("#")
    lenght_list.append(len(sub_list))
    for j in range(len(sub_list)):
        if j%12 ==0:
            title_list.append(sub_list[j])
        if j%12==1:
            company_list.append(sub_list[j])
        if j%12==2:
            salary_list.append(sub_list[j])
        if j%12==3:
            location_list.append(sub_list[j])
        if j%12==4:
            date_list.append(sub_list[j])
        if j%12==5:
            cap_list.append(sub_list[j])
        if j%12==6:
            nganh_list.append(sub_list[j])
        if j%12==7:
            kinnghiem_list.append(sub_list[j])
        if j%12==8:
            hinhthuc_list.append(sub_list[j])
        if j%12==9:
            yeucau_list.append(sub_list[j])
        if j%12==10:
            bangcap_list.append(sub_list[j])
        if j%12==11:
            link_list.append(sub_list[j])

#--------------------------Them duoi "html"----------------------------------------------------------
for i in range(len(link_list)):
    link_list[i] = link_list[i] + "html"

for i in range(len(cap_list)):
    cap_list[i] = cap_list[i].lower()

cap_set = set(cap_list)
print(cap_set)

# with open("kiemtratruongdulieu.txt", "w", encoding="utf8") as file:
#     for m in yeucau_list:
#         file.write(m + "\n")