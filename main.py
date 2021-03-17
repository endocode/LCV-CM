import urllib.request
import requests, json
from LCVlib.verify import *
from LCVlib.testlists import JSONPathList, GitHubURLList


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
index = 8
URL=GitHubURL[index]
JSON=JSONPath[index]

OutboundLicense = retrieveOutboundLicense(URL)
OutboundLicense = CheckOutboundLicense(OutboundLicense)
license_list = InboundLicenses(JSON)

verificationList = compare(license_list, OutboundLicense)
print("Print verification list:")
print(verificationList)
