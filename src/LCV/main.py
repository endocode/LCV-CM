from LCVlib.verify import retrieveOutboundLicense, CheckOutboundLicense, InboundLicenses, compare
from LCVlib.testlists import JSONPathList, GitHubURLList
import sys

JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
#index = int(str(sys.argv), base=10)
# To fix this error, because if there are no args, this control doesn't function.
if len(sys.argv[1]) > 0:
    index = int(sys.argv[1], base=10)
else:
    index = 19

URL = GitHubURL[index]
JSON = JSONPath[index]

OutboundLicense = retrieveOutboundLicense(URL)
OutboundLicense = CheckOutboundLicense(OutboundLicense)
if OutboundLicense is not None:
    license_list = InboundLicenses(JSON)
    verificationList = compare(license_list, OutboundLicense)
    print("Print verification list:")
    print(verificationList)
