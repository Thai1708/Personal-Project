import pandas as pd

with open('data_carreerbuilder_1.txt', 'r', encoding='utf8') as file:
    data = file.read()

list_data = data.split("html#")
list_data.pop()

# print(len(list_data))
for i in range(len(list_data)):
    list_data[i] = list_data[i].replace('\n', '')
    
title_list = []
company_list = []
salary_list = []
location_list = []
date_list = []
cap_list = []
nganh_list = []
hinhthuc_list = []
kinnghiem_list = []
yeucau_list = []
khac_list = []
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
            khac_list.append(sub_list[j])
        if j%12==11:
            link_list.append(sub_list[j])

#--------------------------Them duoi "html"----------------------------------------------------------
for i in range(len(link_list)):
    link_list[i] = link_list[i] + "html"

#--------------------------Sua lai cot cap bac do khong giong cau truc web---------------------------
count = 0
for i in range(len(cap_list)):
    if cap_list[i][:2].isdigit():
        # print(i+1)
        cap_list[i] = kinnghiem_list[i]

#--------------------------Sua lai cot kinh nghiem do khong giong cau truc web-----------------------
for i in range(len(kinnghiem_list)):
    if kinnghiem_list[i][-3:] != "Năm":
        kinnghiem_list[i] = "Not Define"


for i in range(len(cap_list)):
    cap_list[i] = cap_list[i].lower()

cap_set = set(cap_list)
print(cap_set)
# print(len(title_list))
# print(len(company_list))
# print(len(salary_list))
# print(len(location_list))
# print(len(date_list))
# print(len(cap_list))
# print(len(nganh_list))
# print(len(kinnghiem_list))
# print(len(yeucau_list))
# print(len(khac_list))
# print(len(link_list))
# print(len(hinhthuc_list)) 

# df = pd.DataFrame(list(zip(title_list, company_list, salary_list, location_list,  date_list, cap_list, nganh_list, kinnghiem_list, hinhthuc_list, yeucau_list, khac_list, link_list)), columns = ['Tên công việc', 'Công ty', 'Lương','Địa điểm', 'Ngày tháng', 'Cấp bậc', 'Ngành nghề', 'Kinh nghiệm', 'Hình thức', 'Yêu cầu', 'Khác',  'Link'])
# df.to_csv('clean_data_careerbuilder_1.csv', index=False)