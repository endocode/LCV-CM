import urllib.request
import requests, json
from validate import validate
from validate import SPDXIdMapping


def retrieveOutboundLicense(url):
    response = requests.get(url).json()
    content = response['license']['spdx_id']
    return content

print("Started Reading JSON report")
with open("json/dockerfile-maven.json", "r") as read_file:
    data = json.load(read_file)#dict
    license_list = []
    for i in data['payload']['fileMetadata']:
        for x in (i['licenses']):
              if not x in license_list:
                  license_list.append(x)
print("Finished reading JSON report")
print("###################")

GitHubURL = list()

GitHubURL.append('https://api.github.com/repos/hope-for/hope-boot/license')
GitHubURL.append('https://api.github.com/repos/spotify/docker-maven-plugin/license')
GitHubURL.append('https://api.github.com/repos/spotify/dockerfile-maven/license')


OutboundLicense = retrieveOutboundLicense(GitHubURL[2])

print("The outbound license for the project is: "+OutboundLicense)

if len(license_list)==1:
    print("The only inbound license detected is:")
    print(license_list[0])
else:
    print("The inbound licenses found are:")
    print(license_list)

license_list_SPDX = SPDXIdMapping(license_list)

if len(license_list_SPDX)==1:
    print("The SPDX id for the only inbound license detected is:")
    print(license_list_SPDX[0])
else:
    print("The SPDX IDs for the inbound licenses found are:")
    print(license_list_SPDX)


print("#################")
print("Running the license compliance verification:")

validate(license_list_SPDX, OutboundLicense)
print("#################")
