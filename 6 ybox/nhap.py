# my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
# print(my_dict)


# sortedDict = sorted(my_dict)

# print(sortedDict)


hinhthuc = 10
nganh = 1
location = 7
salary = 4
kinhnghiem = 13
list_index_of_field = [hinhthuc, nganh, location, salary, kinhnghiem]
list_index_of_field.sort()
list_index_of_field.append(30)
print(list_index_of_field)
index_hinhthuc = list_index_of_field.index(hinhthuc)
index_nganh = list_index_of_field.index(nganh)
index_location = list_index_of_field.index(location)
index_salary = list_index_of_field.index(salary)
index_kinhnghiem = list_index_of_field.index(kinhnghiem)

print(index_hinhthuc)
print(index_kinhnghiem)
print(index_location)
print(index_salary)
print(index_nganh)

