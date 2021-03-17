import urllib.request
import requests, json, time, sys
from LCVlib.verify import *
from LCVlib.testlists import JSONPathList, GitHubURLList


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
index = 0
t = 10

#while url in GitHubURL:
while index < len(GitHubURL):
    url = GitHubURL[index]
    print("#################")
    print("##Running test number "+str(index))
    print("#################")
    OutboundLicense = retrieveOutboundLicense(url)
    license_list = InboundLicenses(JSONPath[index])
    index += 1

    compare(license_list, OutboundLicense)
    runtimer(t)
