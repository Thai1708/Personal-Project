import pandas as pd

with open('data_topcv.txt', 'r', encoding='utf8') as file:
    data = file.read()

list_data = data.split("#")
list_data.pop()
# print(len(list_data))
for i in range(len(list_data)):
    list_data[i] = list_data[i].replace('\n', '')

# print(len(list_data))
    
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
soluong_list = []
link_list = []
bangcap_list = []

lenght_list = []

for i in range(len(list_data)):
    if i%12 ==0:
        title_list.append(list_data[i])
    if i%12==1:
        company_list.append(list_data[i])
    if i%12==2:
        salary_list.append(list_data[i])
    if i%12==3:
        location_list.append(list_data[i])
    if i%12==4:
        date_list.append(list_data[i])
    if i%12==5:
        cap_list.append(list_data[i])
    if i%12==6:
        nganh_list.append(list_data[i])
    if i%12==7:
        kinnghiem_list.append(list_data[i])
    if i%12==8:
        hinhthuc_list.append(list_data[i])
    if i%12==9:
        yeucau_list.append(list_data[i])
    if i%12==10:
        soluong_list.append(list_data[i])
    if i%12==11:
        link_list.append(list_data[i])

##################################ETL BANG CAP TU YEU CAU#################################################
# for i in range(len(yeucau_list)):
#     yeucau_list[i] = yeucau_list[i].lower()

# for yc in yeucau_list:
#     if "cao đẳng" in yc or "trung cấp" in yc:
#         bangcap_list.append("Cao đẳng")
#     elif "đại học" in yc:
#         bangcap_list.append("Đại học")
#     else:
#         bangcap_list.append("Không yêu cầu")

# print(bangcap_list)
###########################################################################################################

##################################ĐỔ DỮ LIỆU VÀO DATABASE#################################################

# do_dai = []
# for i in range(len(yeucau_list)):
#     do_dai.append(len(yeucau_list[i]))
# print(max(do_dai))
    
# index_= 1
# for yc in yeucau_list[:30]:
#     print(f"{index_}: {yc}")
#     index_ += 1

# import mysql.connector

# conn = mysql.connector.connect(
#     host='localhost',
#     port = 3306,
#     user= 'root',
#     password='Pthai332277@',
#     database= 'test'
# )
# cursor = conn.cursor()

# sql = 'INSERT IGNORE INTO Stg_ThongTin_raw(Ten, Cong_ty, Luong, Dia_diem, Ngay_thang, Cap_bac, Nganh_nghe, Kinh_nghiem, Hinh_thuc, Yeu_cau, So_luong) VALUES (%s, %s, %s, %s,%s,%s,%s, %s, %s, %s, %s)'
# for i in range(len(kinnghiem_list)):
#     cursor.execute(sql, (title_list[i], company_list[i], salary_list[i], location_list[i], date_list[i], cap_list[i], nganh_list[i], kinnghiem_list[i], hinhthuc_list[i], yeucau_list[i], soluong_list[i]))
#     conn.commit()
###########################################################################################################

##################################ETL TRUONG KINH NGHIEM TU TRUONG KINH NGHIEM############################
# for i in range(len(kinnghiem_list)):
#     kinnghiem_list[i] = kinnghiem_list[i].lower()
# for i in range(len(kinnghiem_list)):
#     if "không yêu cầu kinh nghiệm" in kinnghiem_list[i]:
#         kinnghiem_list[i] = "Không yêu cầu"
#     elif kinnghiem_list[i][0:1] == "1" or kinnghiem_list[i][0:1] == "2" or kinnghiem_list[i][0:1] == "3":
#         kinnghiem_list[i] = "1-3 năm"
#     elif kinnghiem_list[i][0:1] == "4" or kinnghiem_list[i][0:1] == "5":
#         kinnghiem_list[i] = "3-5 năm"
#     elif "dưới" in kinnghiem_list[i]:
#         kinnghiem_list[i] = "Dưới 1 năm"
#     else:
#         kinnghiem_list[i] = "Trên 5 năm"
# print(kinnghiem_list)
#####################################ETL TRUONG CAP BAC TU TRUONG CAP BAC##############################
for i in range(len(cap_list)):
    cap_list[i] = cap_list[i].lower()
for i in range(len(cap_list)):
    if cap_list[i] == "quản lý / giám sát" or cap_list[i] == "trưởng nhóm" or cap_list[i] == "trưởng/phó phòng":
        cap_list[i] = "quản lý cấp trung"
    if cap_list[i] == "phó giám đốc" or cap_list[i] == "giám đốc" or cap_list[i] == "trưởng chi nhánh":
        cap_list[i] = "quản lý cấp cao"


##########################################################################################################
cap_set = set(cap_list)
print(cap_set)


key_list = ["executive", "content", "seo", "digital", "brand", "trade"]
map_title_list = []
for i in range(len(title_list)):
    if cap_list[i] == "nhân viên":
        for k in key_list:
            flag = 0
            if k in title_list:
                map_title_list.append(k)
                flag = 1
                break
        if flag == 0:
            map_title_list.append(title_list[i])



with open("kiemtratruongdulieu.txt", "w", encoding="utf8") as file:
    for m in map_title_list:
        m = m.lower()
        file.write(m + "\n")

# key_list = ["executive", "content", "seo", "digital", "brand", "trade"]
# with open("kiemtratruongdulieu.txt", "w", encoding="utf8") as file:
#     for i in range(len(title_list)):
#         if cap_list[i] == "nhân viên":
#             for k in key_list:
#                 if k in title_list[i]:
#                     title_list[i]  = "MAP"
#                     file.write(title_list[i] + "\n")
                    



########################KHONG SU DUNG NỮA#################################################################

# df = pd.DataFrame(list(zip(title_list, company_list, salary_list, location_list,  date_list, cap_list, nganh_list, kinnghiem_list, hinhthuc_list, yeucau_list, soluong_list, link_list)), columns = ['Tên công việc', 'Công ty', 'Lương','Địa điểm', 'Ngày tháng', 'Cấp bậc', 'Ngành nghề', 'Kinh nghiệm', 'Hình thức', 'Yêu cầu', 'Số lượng',  'Link'])
# df.to_csv('clean_data_topcv.csv', index=False)



# print("Title: "+ str(len(title_list)))
# print("Company: "+ str(len(company_list)))
# print("Salary: "+ str(len(salary_list)))
# print("Location: "+ str(len(location_list)))
# print("Date: "+ str(len(date_list)))
# print("Cap bac: "+ str(len(cap_list)))
# print("Nganh nghe: "+ str(len(nganh_list)))
# print("Kinh nghiem: "+ str(len(kinnghiem_list)))
# print("Hinh thuc: "+ str(len(hinhthuc_list)))
# print("Yeu cau: "+ str(len(yeucau_list)))
# print("So luong: "+ str(len(soluong_list)))
# print("Link: "+ str(len(link_list)))

# for i in range(1000, 1200):
#     print(f"{i+1}: {title_list[i]}")
# #--------------------------Them duoi "html"----------------------------------------------------------
# for i in range(len(link_list)):
#     link_list[i] = link_list[i] + "html"
# #--------------------------Sua lai cot cap bac do khong giong cau truc web---------------------------
# count = 0
# for i in range(len(cap_list)):
#     if cap_list[i][:2].isdigit():
#         # print(i+1)
#         cap_list[i] = kinnghiem_list[i]

# #--------------------------Sua lai cot kinh nghiem do khong giong cau truc web-----------------------
# for i in range(len(kinnghiem_list)):
#     if kinnghiem_list[i][-3:] != "Năm":
#         kinnghiem_list[i] = "Not Define"
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
