import json
from validate import validate


print("Started Reading JSON report")
with open("json/javacpp.json", "r") as read_file:
    data = json.load(read_file)#dict
    license_list = []
    for i in data['payload']['fileMetadata']:
        for x in (i['licenses']):
              if not x in license_list:
                  license_list.append(x)
            # print(i['licenses'][1])

print("Finished reading JSON report")
print("Licenses found are:")
print(license_list)
validate(license_list)
