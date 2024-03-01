# importing the module
import csv

def unique(list1):
 
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    # for x in unique_list:
    #     print(f"{x},")
		
    return unique_list

# open the file in read mode
filename = open('1 vietnamwork/clean_data_vietnamwork.csv', 'r', encoding='utf8')

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
skill_list = []
cap_list = []

# iterating over each row and append
# values to empty list
for col in file:
	skill_list.append(col['Kỹ năng'])
	cap_list.append(col['Cấp bậc'])

all_key_words_skill = []
all_key_words_cap = []
for i in range(len(skill_list)):
	sublist = skill_list[i].split(",")
	for j in range(len(sublist)):
		all_key_words_skill.append(sublist[j])

for i in range(len(all_key_words_skill)):
	all_key_words_skill[i] = str(all_key_words_skill[i]).strip()
	# print(all_key_words[i])
	
unique_list = unique(all_key_words_skill)
print(len(unique_list))
for u in unique_list:
	print(f"{u},", end=" ")