import pandas as pd

class Information:
    def __init__(self, titles, companys, salarys, locations, dates, caps, nganh_nghes, ky_nangs, links):
        self.titles = titles
        self.companys = companys
        self.salarys = salarys
        self.locations = locations
        self.dates = dates
        self.caps = caps
        self.nganh_nghes = nganh_nghes
        self.ky_nangs = ky_nangs
        self.links = links

with open('data.txt', 'r', encoding='utf8') as file:
    datas = file.readlines()


for i in range(len(datas[:750])):
    datas[i] = datas[i].replace('<span class="content">\n', '')
    datas[i]=datas[i].replace("</span>\n", '')
    datas[i]=datas[i].replace("\n", '')
    datas[i]=datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=17">', '')
    datas[i] = datas[i].replace('</a>', '')
    datas[i] = datas[i].strip()

new_list = [item for item in datas if item != '']
print(new_list)


title_list = []
company_list = []
salary_list = []
location_list = []
date_list = []
cap_list = []
nganh_list = []
kynang_list = []
link_list = []
#-----------------------------------------------Gan gia tri vao class
for i in range(450):
    if i%9 == 0:
        title_list.append(new_list[i])
    if i%9 == 1:
        company_list.append(new_list[i])
    if i%9 == 2:
        salary_list.append(new_list[i])
    if i%9 == 3:
        location_list.append(new_list[i])
    if i%9 == 4:
        date_list.append(new_list[i])
    if i%9 == 5:
        cap_list.append(new_list[i])
    if i%9 == 6:
        nganh_list.append(new_list[i])
    if i%9 == 7:
        kynang_list.append(new_list[i])
    if i%9 == 8:
        link_list.append(new_list[i])


df = pd.DataFrame(list(zip(title_list, company_list, salary_list, location_list,  date_list, cap_list, nganh_list, kynang_list, link_list)), columns = ['Tên công việc', 'Công ty', 'Lương','Địa điểm', 'Ngày tháng', 'Cấp bậc', 'Ngành nghề', 'Kỹ năng', 'Link'])
df.to_csv('clean_data.csv', index=False)
