# linkpages = []
# for i in range(1, 117):
#     linkpage = f'https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?sort=top_related&page={i}'
#     linkpages.append(linkpage)

# with open('linkpage.txt', 'a') as file:
#     for linkpage in linkpages:
#         file.write(linkpage + "\n")

original_strings = [
    '<p>• Specific knowledge of System Center Operations Manager 2016 and subsequent versions – A plus, similar monitoring products.</p>',
    '<p>• Specific Knowledge of System Center Service Manager 2016 and subsequent versions – a plus, similar ticketing products.</p>',
    '<p>• Knowledge of System Center Orchestrator 2016 and subsequent versions – a plus, similar orchestration products.</p>',
    '<p>• Specific Knowledge of System Center Virtual Machine Manager 2016 and subsequent versions – a plus, similar Machine Manager products.</p>',
    '<p>• Knowledge of Management Pack Technology, Overrides, Rules and Monitors.\n</p>',
    '<p>• Experience with SQL administration/configuration including basic knowledge of TSQL syntaxis, WMI functionality and queries.</p>',
    '<p>• Knowledge of Windows and Linux operating systems.\n</p>',
    '<p>• Knowledge of Exchange, AD, DNS, DHCP, TCP/IP, Network and Azure.\n</p>',
    '<p>• ITIL certification/MOF are pluses.&nbsp;</p>'
]

# Loại bỏ các ký tự từ mỗi chuỗi trong mảng
cleaned_strings = [s.replace('</p>', '').replace('<p>', '').replace('\n', '') for s in original_strings]

# In mảng kết quả
print(cleaned_strings)
with open("require.txt", "w") as file:
    file.write('<>'.join(cleaned_strings))
