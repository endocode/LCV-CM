from LCVlib.verify import retrieveOutboundLicense, CheckOutboundLicense, InboundLicenses, compare
from LCVlib.testlists import JSONPathList, GitHubURLList


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
index = 1
URL = GitHubURL[index]
JSON = JSONPath[index]

OutboundLicense = retrieveOutboundLicense(URL)
OutboundLicense = CheckOutboundLicense(OutboundLicense)
if OutboundLicense is not None:
    license_list = InboundLicenses(JSON)
    verificationList = compare(license_list, OutboundLicense)
    print("Print verification list:")
    print(verificationList)
