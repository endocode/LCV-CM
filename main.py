import json
from validate import validate


print("Started Reading JSON report")
with open("json/json-iterator.json", "r") as read_file:
    data = json.load(read_file)#dict
    license_list = []
    for i in data['payload']['fileMetadata']:
        if not (i['licenses']) in license_list:
            license_list.append(i['licenses'])
license_list_cleaned = []

#print ("Licenses found in this project are :")
for i in license_list:
    my_string = str(i).replace('[', '')
    my_string = str(my_string).replace(']', '')
    my_string = str(my_string).replace('\'', '')
    license_list_cleaned.append(my_string)

#print(license_list_cleaned)
print("Finished reading JSON report")
print("Licenses found are:")
print(license_list_cleaned)

validate(license_list_cleaned)



# accessing-data-from-a-json-array-in-python
#https://stackoverflow.com/questions/57799042/accessing-data-from-a-json-array-in-python/57799117
#https://www.programiz.com/python-programming/json
