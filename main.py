import urllib.request
import requests, json
from verify import verify
from verify import SPDXIdMapping


def retrieveOutboundLicense(url):
    response = requests.get(url).json()
    content = response['license']['spdx_id']
    if content == "NOASSERTION":
        print("SPDX ID's outbound license not correctly defined for the project: "+GitHubURL[index])
        print("Please use a project with an outbound license defined with its SPDX id")
        exit(0)
    return content
orLater = "or-later"


JSONPath = list()

JSONPath.append('json/hope-boot.json')
JSONPath.append('json/spotify-docker-maven-plugin.json')
JSONPath.append('json/dockerfile-maven.json')
JSONPath.append('json/TelegramBots.json')
JSONPath.append('json/fabric8io-docker-maven-plugin.json')
JSONPath.append('json/webdrivermanager.json')
JSONPath.append('json/git-commit-id-maven-plugin.json')
JSONPath.append('json/javacv.json')
JSONPath.append('json/javacpp.json')


#print(JSONPath)
index = 0

print("#################")
print("Started Reading JSON report")
with open(JSONPath[index], "r") as read_file:
    print("Reading: " + JSONPath[index])
    data = json.load(read_file)#dict
    license_list = []
    for i in data['payload']['fileMetadata']:
        for x in (i['licenses']):
            if not x in license_list:
                license_list.append(x)
print("Finished reading JSON report")
print("###################\n")

GitHubURL = list()

GitHubURL.append('https://api.github.com/repos/hope-for/hope-boot/license')
GitHubURL.append('https://api.github.com/repos/spotify/docker-maven-plugin/license')
GitHubURL.append('https://api.github.com/repos/spotify/dockerfile-maven/license')
#Inbound: GPL3.0 or later
GitHubURL.append('https://api.github.com/repos/rubenlagus/TelegramBots/license')
#index = 4
GitHubURL.append('https://api.github.com/repos/fabric8io/docker-maven-plugin/license')
#links to do https://github.com/bonigarcia/webdrivermanager
# Error 2021/03/10 11:02:13 Received a message: gooooo!!!!!
# 2021/03/10 11:02:14 FASTEN reporter failed: couldn't get FileNodes, rpc error: code = Unavailable desc = connection error: desc = "transport: Error while dialing dial tcp 10.20.13.51:9080: connect: connection refused"
GitHubURL.append('https://api.github.com/repos/bonigarcia/webdrivermanager/license')

#https://github.com/git-commit-id/git-commit-id-maven-plugin
GitHubURL.append('https://api.github.com/repos/git-commit-id/git-commit-id-maven-plugin/license')
GitHubURL.append('https://api.github.com/repos/bytedeco/javacv/license')
#index = 8
GitHubURL.append('https://api.github.com/repos/bytedeco/javacpp/license')


OutboundLicense = retrieveOutboundLicense(GitHubURL[index])

print("The outbound license for the project is: "+OutboundLicense)
if orLater in OutboundLicense:
    print("The usage of `'or later' is not supported. \n Please specify a license version instead of using `'or later'` notation.")
    exit(0)

if len(license_list)==1:
    print("\nThe only inbound license detected is:")
    print(license_list[0])
else:
    print("\nThe inbound licenses found are:")
    print(license_list)

license_list_SPDX = SPDXIdMapping(license_list)

if len(license_list_SPDX)==1:
    print("\nThe SPDX id for the only inbound license detected is:")
    print(license_list_SPDX[0])
else:
    print("\nThe SPDX IDs for the inbound licenses found are:")
    print(license_list_SPDX)


print("\n#################")
print("Running the license compliance verification:")
print("#################")

verificationList = verify(license_list_SPDX, OutboundLicense)

notCompatible = "is not compatible"
Compatible = "is compatible"
for element in verificationList:
    if notCompatible in element:
        print("YOUR PACKAGE IS NOT COMPLIANT because:\n"+element)
    if Compatible in element:
        print("\n"+element+"\nThis allow you to use this inbound license in your package.\n")

#print(verificationList)
