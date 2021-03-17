# import urllib.request
# import requests
# import json
# import time
# import sys
from LCVlib.verify import retrieveOutboundLicense, InboundLicenses, compare, runtimer, CheckOutboundLicense
from LCVlib.testlists import JSONPathList, GitHubURLList


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
index = 4
t = 10
empty = ""
orLater = "or-later"
# while url in GitHubURL:
while index < len(GitHubURL):
    url = GitHubURL[index]
    print("#################")
    print("##Running test number "+str(index))
    print("#################")
    OutboundLicense = retrieveOutboundLicense(url)
    OutboundLicense = CheckOutboundLicense(OutboundLicense)
    if OutboundLicense is not None:
        license_list = InboundLicenses(JSONPath[index])
        compare(license_list, OutboundLicense)
    runtimer(t)
    index += 1
