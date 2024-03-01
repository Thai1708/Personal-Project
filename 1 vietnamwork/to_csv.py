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

with open('1 vietnamwork/data_nghiencuuvaphantichthitruong.txt', 'r', encoding='utf8') as file:
    datas = file.readlines()
print(len(datas))


for i in range(len(datas)):
    datas[i] = datas[i].replace('<span class="content">\n', '')
    datas[i]=datas[i].replace("</span>\n", '')
    datas[i]=datas[i].replace("\n", '')
    datas[i]=datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=17">', '')
    datas[i] = datas[i].replace('</a>', '')
    datas[i] = datas[i].replace('<strong class="text-primary text-lg">', '')
    datas[i] = datas[i].replace('</strong>', '')
    #----------------------------------Clean Vung Mien------------------------------------------------
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-ho-chi-minh-v29-vn" title="Việc làm tại Hồ Chí Minh">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-hai-phong-v28-vn" title="Việc làm tại Hải Phòng">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-ha-noi-v24-vn" title="Việc làm tại Hà Nội">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-binh-duong-v11-vn" title="Việc làm tại Bình Dương">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-da-nang-v17-vn" title="Việc làm tại Đà Nẵng">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-dong-nai-v19-vn" title="Việc làm tại Đồng Nai">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-can-tho-v15-vn" title="Việc làm tại Cần Thơ">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-nghe-an-v41-vn" title="Việc làm tại Nghệ An">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-hung-yen-v32-vn" title="Việc làm tại Hưng Yên">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-thua-thien-hue-v57-vn" title="Việc làm tại Thừa Thiên Huế">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-dong-thap-v20-vn" title="Việc làm tại Đồng Tháp">Đồng Tháp', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-quoc-te-v70-vn" title="Việc làm tại Quốc tế">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-lam-dong-v36-vn" title="Việc làm tại Lâm Đồng">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-dbscl-v71-vn" title="Việc làm tại ĐBSCL">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-quang-nam-v47-vn" title="Việc làm tại Quảng Nam">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-tra-vinh-v59-vn" title="Việc làm tại Trà Vinh">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-ca-mau-v14-vn" title="Việc làm tại Cà Mau">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-vinh-long-v62-vn" title="Việc làm tại Vĩnh Long">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-bac-giang-v5-vn" title="Việc làm tại Bắc Giang">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-khanh-hoa-v33-vn" title="Việc làm tại Khánh Hòa">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-quang-ninh-v49-vn" title="Việc làm tại Quảng Ninh">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-phu-tho-v44-vn" title="Việc làm tại Phú Thọ">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-tien-giang-v58-vn" title="Việc làm tại Tiền Giang">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-binh-dinh-v10-vn" title="Việc làm tại Bình Định">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-thai-binh-v54-vn" title="Việc làm tại Thái Bình">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-thai-nguyen-v55-vn" title="Việc làm tại Thái Nguyên">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-vinh-phuc-v63-vn" title="Việc làm tại Vĩnh Phúc">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-hai-duong-v27-vn" title="Việc làm tại Hải Dương">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-binh-phuoc-v12-vn" title="Việc làm tại Bình Phước">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-dak-lak-v18-vn" title="Việc làm tại Đắk Lắk">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-binh-thuan-v13-vn" title="Việc làm tại Bình Thuận">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-ha-nam-v23-vn" title="Việc làm tại Hà Nam">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-ba-ria-vung-tau-v3-vn" title="Việc làm tại Bà Rịa - Vũng Tàu">', '')
    datas[i] = datas[i].replace('<a itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress" href="https://www.vietnamworks.com/viec-lam-tai-quang-ngai-v48-vn" title="Việc làm tại Quảng Ngãi">', '')
    #-----------------------------------Clean Nganh Nghe-----------------------------------------------
    datas[i] = datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=28">', '')
    datas[i] = datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=21">', '')
    datas[i] = datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=19">', '')
    datas[i] = datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=26">', '')
    datas[i] = datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=9">', '')
    datas[i] = datas[i].replace('<a property="item" typeof="WebPage" href="https://www.vietnamworks.com/viec-lam?g=24">', '')

    datas[i] = datas[i].strip()

new_list = [item for item in datas if item != '']

#------------------------------------------Test Data in Each Column----------------------------------
for i in range(len(new_list)):
    if i%9 == 0:
        print(str(i+1), new_list[i])
#------------------------------------------Them dong bi thieu----------------------------------------
# for i in range(len(new_list)):
#     print(str(i+1), new_list[i])
# new_list.insert(408, 'Not Define')
# for i in range(len(new_list)):
#     if i%9 == 0:
#         print(str(i+1), new_list[i])

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
for i in range(len(new_list)):
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


# df = pd.DataFrame(list(zip(title_list, company_list, salary_list, location_list,  date_list, cap_list, nganh_list, kynang_list, link_list)), columns = ['Tên công việc', 'Công ty', 'Lương','Địa điểm', 'Ngày tháng', 'Cấp bậc', 'Ngành nghề', 'Kỹ năng', 'Link'])
# df.to_csv('clean_data_nghiencuuvaphantichthitruong_3.csv', index=False, encoding='utf-8')
        
for i in range(len(cap_list)):
    cap_list[i] = cap_list[i].lower()

cap_set = set(cap_list)
print(cap_set)
# data6.txt
