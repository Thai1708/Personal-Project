import pandas as pd

with open('data_vieclam24h.txt', 'r', encoding='utf8') as file:
    data = file.read()

list_data = data.split("html#")
list_data.pop()
print(len(list_data))

for i in range(len(list_data)):
    list_data[i] = list_data[i].replace('\n', '')

title_list = []
company_list = []
salary_list = []
location_list = []
date_list = []
block_list = []
yeucau_list = []
link_list = []

for i in range(len(list_data)):
    sub_list = list_data[i].split("#")
    # lenght_list.append(len(sub_list))
    for j in range(len(sub_list)):
        if j%8 ==0:
            title_list.append(sub_list[j])
        if j%8==1:
            company_list.append(sub_list[j])
        if j%8==2:
            salary_list.append(sub_list[j])
        if j%8==3:
            location_list.append(sub_list[j])
        if j%8==4:
            date_list.append(sub_list[j])
        if j%8==5:
            block_list.append(sub_list[j])
        if j%8==6:
            yeucau_list.append(sub_list[j])
        if j%8==7:
            link_list.append(sub_list[j])
clean_date_list = []
for i in range(len(date_list)):
    date_split = date_list[i].split(" ")
    clean_date_list.append(date_split[0])

count  =1
for i in range(len(block_list)):
    # block_list[i] = block_list[i].replace("Ngày đăng", "##")
    block_list[i] = block_list[i].replace("Cấp bậc", "##")
    # block_list[i] = block_list[i].replace("Cấp bậc", "##")
    block_list[i] = block_list[i].replace("Số lượng tuyển", "##")
    block_list[i] = block_list[i].replace("Hình thức làm việc", "##")
    # block_list[i] = block_list[i].replace("Yêu cầu bằng cấp", "##")
    block_list[i] = block_list[i].replace("Yêu cầu kinh nghiệm", "##")
    block_list[i] = block_list[i].replace("Ngành nghề", "##")

capbac_list = []
soluong_list = []
hinhthuc_list = []
nganhnghe_list = []
bangcap_list = []
kinhnghiem_list = []

for i in range(len(block_list)):
    sub_list_block = block_list[i].split("##")
    # Filter cap bac
    if "Yêu cầu giới tính" in sub_list_block[1]:
        index_ycgt = sub_list_block[1].index("Yêu cầu giới tính")
        capbac = sub_list_block[1][:(index_ycgt)]
        capbac_list.append(capbac)
    else:
        capbac = sub_list_block[1]
        capbac_list.append(capbac)
    # Filter hinh thuc va bang cap
    if ("Độ tuổi" in sub_list_block[3]) and ("Yêu cầu bằng cấp" in sub_list_block[3]):
        index_dt = sub_list_block[3].index("Độ tuổi")
        hinhthuc = sub_list_block[3][:(index_dt)]
        hinhthuc_list.append(hinhthuc)
        index_ycbc = sub_list_block[3].index("Yêu cầu bằng cấp")
        bangcap = sub_list_block[3][(index_ycbc+16):]
        bangcap_list.append(bangcap)
    elif ("Độ tuổi" in sub_list_block[3]) and ("Yêu cầu bằng cấp" not in sub_list_block[3]):
        index_dt = sub_list_block[3].index("Độ tuổi")
        hinhthuc = sub_list_block[3][:(index_dt)]
        hinhthuc_list.append(hinhthuc)
        bangcap_list.append("Không yêu cầu bằng cấp")

    elif ("Độ tuổi" not in sub_list_block[3]) and ("Yêu cầu bằng cấp" in sub_list_block[3]):
        index_ycbc = sub_list_block[3].index("Yêu cầu bằng cấp")
        hinhthuc = sub_list_block[3][:(index_ycbc)]
        hinhthuc_list.append(hinhthuc)

        bangcap = sub_list_block[3][(index_ycbc+16):]
        bangcap_list.append(bangcap)
    else:
        hinhthuc_list.append(sub_list_block[3])
        bangcap_list.append("Không yêu cầu bằng cấp")

    # Filter so luong
    soluong_list.append(sub_list_block[2])

    #Filter nganh nghe
    nganhnghe_list.append(sub_list_block[5])

    #Filter kinh nghiem
    kinhnghiem_list.append(sub_list_block[4])
#####################################################################
# with open("kiemtratruongdulieu.txt", "w", encoding="utf8") as file:
#     for m in block_list:
#         file.write(m + "\n")
    
for i in range(len(capbac_list)):
    capbac_list[i] = capbac_list[i].lower()

cap_set = set(capbac_list)
print(cap_set)

# df = pd.DataFrame(list(zip(title_list, company_list, bangcap_list, salary_list, location_list,  clean_date_list, capbac_list, nganhnghe_list, kinhnghiem_list, hinhthuc_list, soluong_list, yeucau_list, link_list)), columns = ['Tên công việc', 'Công ty', 'Bằng cấp', 'Lương','Địa điểm', 'Ngày tháng', 'Cấp bậc', 'Ngành nghề', 'Kinh nghiệm', 'Hình thức', 'Số lượng', 'Yêu cầu',  'Link'])
# df.to_csv('clean_data_vieclam24h.csv', index=False)