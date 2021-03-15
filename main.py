import urllib.request
import requests, json
from verify import verify, compare, SPDXIdMapping, retrieveOutboundLicense, InboundLicenses, runtimer
from testlists import JSONPathList, GitHubURLList


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
index = 8
URL=GitHubURL[index]
JSON=JSONPath[index]

OutboundLicense = retrieveOutboundLicense(URL)
license_list = InboundLicenses(JSON)

compare(license_list, OutboundLicense)
