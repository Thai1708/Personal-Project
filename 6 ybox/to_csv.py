import pandas as pd

with open('data_ybox.txt', 'r', encoding='utf8') as file:
    data = file.read()

list_data = data.split("#html")
list_data.pop()
print(len(list_data))

for i in range(len(list_data)):
    list_data[i] = list_data[i].replace('\n', '')

print(len(list_data))

title_company_list = []
block_list = []
date_list = []
yeucau_list = []
link_list = []

for i in range(len(list_data)):
    sub_list = list_data[i].split("#")
    # lenght_list.append(len(sub_list))
    for j in range(len(sub_list)):
        if j%5 ==0:
            title_company_list.append(sub_list[j])
        if j%5==1:
            block_list.append(sub_list[j])
        if j%5==2:
            date_list.append(sub_list[j])
        if j%5==3:
            yeucau_list.append(sub_list[j])
        if j%5==4:
            link_list.append(sub_list[j])




hinhthuc_list = []
nganhnghe_list = []
location_list = []
salary_list = []
kinhnghiem_list = []

for i in range(len(block_list)):
    hinhthuc_postion = block_list[i].index("Tính chất công việc:")
    nganhnghe_postion = block_list[i].index("Chuyên môn:")
    location_postion = block_list[i].index("Địa điểm:")
    salary_postion = block_list[i].index("Mức lương:")
    kinhnghiem_postion = block_list[i].index("Kinh nghiệm:")
    # Theo thu tu cac truong nhu phia duoi
    list_position_of_field = [hinhthuc_postion, nganhnghe_postion, location_postion, salary_postion, kinhnghiem_postion]
    list_position_of_field.sort()
    list_position_of_field.append(len(block_list[i]))
    # Chi so vi tri tung truong trong mang da sap xep
    index_hinhthuc = list_position_of_field.index(hinhthuc_postion)
    index_nganhnghe = list_position_of_field.index(nganhnghe_postion)
    index_location = list_position_of_field.index(location_postion)
    index_salary = list_position_of_field.index(salary_postion)
    index_kinhnghiem = list_position_of_field.index(kinhnghiem_postion)

    hinhthuc_text = block_list[i][list_position_of_field[index_hinhthuc]:list_position_of_field[index_hinhthuc+1]]
    hinhthuc_list.append(hinhthuc_text)

    nganhnghe_text = block_list[i][list_position_of_field[index_nganhnghe]:list_position_of_field[index_nganhnghe+1]]
    nganhnghe_list.append(nganhnghe_text)

    location_text = block_list[i][list_position_of_field[index_location]:list_position_of_field[index_location+1]]
    location_list.append(location_text)

    salary_text = block_list[i][list_position_of_field[index_salary]:list_position_of_field[index_salary+1]]
    salary_list.append(salary_text)

    kinhnghiem_text = block_list[i][list_position_of_field[index_kinhnghiem]:list_position_of_field[index_kinhnghiem+1]]
    kinhnghiem_list.append(kinhnghiem_text)

for i in range(len(location_list)):
    location_list[i] = location_list[i].replace("Địa điểm: ", "")
    location_list[i] = location_list[i].replace(" - ", "")

    hinhthuc_list[i] = hinhthuc_list[i].replace("Tính chất công việc: ", "")
    hinhthuc_list[i] = hinhthuc_list[i].replace(" - ", "")

    salary_list[i] = salary_list[i].replace("Mức lương: ", "")
    if salary_list[i][-3:] == " - ":
        salary_list[i] = salary_list[i][:-3]

    nganhnghe_list[i] = nganhnghe_list[i].replace("Chuyên môn: ", "")
    nganhnghe_list[i] = nganhnghe_list[i].replace(" - ", "")

    if "phải có kinh nghiệm" in kinhnghiem_list[i]:
        kinhnghiem_list[i] = "6 tháng"
    else:
        kinhnghiem_list[i] = "0"

title_list = []
company_list = []
for i in range(len(title_company_list)):
    title_company_list[i] = title_company_list[i].lower()
    if "tuyển dụng " not in title_company_list[i]:
        title_company_list[i] = title_company_list[i] + "tuyển dụng "

for i in range(len(title_company_list)):
    list_split = title_company_list[i].split("tuyển dụng ")
    ngoac_index = list_split[0].index("]")
    list_split[0] = list_split[0][ngoac_index+2:]
    company_list.append(list_split[0])
    title_list.append(list_split[1])



# with open("kiemtratruongdulieu.txt", "w", encoding="utf8") as file:
#     for m in company_list:
#         file.write(m + "\n")

# df = pd.DataFrame(list(zip(title_list, company_list, salary_list, location_list, date_list, nganhnghe_list, kinhnghiem_list, hinhthuc_list, yeucau_list, link_list)), columns = ['Tên công việc', 'Công ty',  'Lương','Địa điểm', 'Ngày tháng',  'Ngành nghề', 'Kinh nghiệm', 'Hình thức', 'Yêu cầu',  'Link'])
# df.to_csv('clean_data_ybox.csv', index=False)