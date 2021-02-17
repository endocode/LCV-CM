import json
from connect import connect


print("Started Reading JSON report")
with open("javacpp.json", "r") as read_file:
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

connect(license_list_cleaned)



# accessing-data-from-a-json-array-in-python
#https://stackoverflow.com/questions/57799042/accessing-data-from-a-json-array-in-python/57799117
#https://www.programiz.com/python-programming/json
