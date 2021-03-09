import json
from validate import validate
from validate import SPDXIdMapping


print("Started Reading JSON report")
with open("json/javacv.json", "r") as read_file:
    data = json.load(read_file)#dict
    license_list = []
    for i in data['payload']['fileMetadata']:
        for x in (i['licenses']):
              if not x in license_list:
                  license_list.append(x)

print("Finished reading JSON report")
print("###################")
print("Licenses found are:")
print(license_list)

license_list_SPDX = SPDXIdMapping(license_list)

print("The SPDX IDs are:")
print(license_list_SPDX)

validate(license_list_SPDX)
#validate(license_list)
