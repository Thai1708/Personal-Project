mystring = "pham van thai"
print(mystring.index('a'))

# <h2 class="post-title"><a target="_blank" href="/tuyendung
# <h2 class="post-title"><a target="_blank" href="/tuyen-dung

with open("html.txt", "r", encoding="utf8") as file:
    datas = file.readlines()

links = []
for data in datas:
    if '<h2 class="post-title"><a target="_blank" href="/tuyen-dung' in data:
        data_split = data.split('<h2 class="post-title"><a target="_blank" href="/tuyen-dung')
        for element in data_split[1:]:
            index_ = element.index('>')
            link = "https://ybox.vn/tuyen-dung" + element[:(index_-1)]
            links.append(link)

for link in links:
    print(link)   
print(len(links))
with open('link_subpage_ybox.txt', 'a') as file:
    for link in links:
        file.write(link + '\n')


#post-content > div:nth-child(2) > div:nth-child(2) > div
#post-content > div:nth-child(2) > div:nth-child(2) > div
#app > div > div:nth-child(2) > div.page-container > div > div > div > div.container-fluid.spp__content > div > div > div > div.col-sm-6.col-xs-12 > div > div > div > div:nth-child(4) > div
#post-content > div:nth-child(2) > div:nth-child(2) > div
#post-content > div:nth-child(2) > div:nth-child(2) > div