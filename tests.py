import urllib.request
import requests, json, time, sys
from verify import verify, compare, SPDXIdMapping, retrieveOutboundLicense, InboundLicenses, runtimer
from testlists import JSONPathList, GitHubURLList


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
index = 3
t = 10

#while url in GitHubURL:
while index < len(GitHubURL):
    print("#################")
    print("##Running test .... ")

    print("\n\nTest number "+str(index)+ " running\n\n ")
    url = GitHubURL[index]
    print(url)
    OutboundLicense = retrieveOutboundLicense(url)
    print(JSONPath[index])
    #print("Test number "+str(index)+" completed.")
    license_list = InboundLicenses(JSONPath[index])
    print(license_list)
    index += 1

    compare(license_list, OutboundLicense)
    runtimer(t)
