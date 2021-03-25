import sys
from LCVlib.testlistsGithubAPI import GitHubURLList
from LCVlib.testlistsJSONfiles import JSONPathList
from LCVlib.verify import retrieveOutboundLicense, CheckOutboundLicense
from LCVlib.verify import InboundLicenses, compare
'''
* SPDX-FileCopyrightText: 2021 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: MIT
'''


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
# index = int(str(sys.argv), base=10)
# To fix this error, because if there are no args, this control doesn't function.
if len(sys.argv[1]) > 0:
    index = int(sys.argv[1], base=10)
else:
    print("No parameter has been included.\n")
    print("Please, insert an integer to identify a pair JSON")
    print("(for the inbound licenses) and GitHub API url (for the outbound license).")

URL = GitHubURL[index]
JSON = JSONPath[index]

OutboundLicense = retrieveOutboundLicense(URL)
OutboundLicense = CheckOutboundLicense(OutboundLicense)
if OutboundLicense is not None:
    InboundLicenses = InboundLicenses(JSON)
    verificationList = compare(InboundLicenses, OutboundLicense)
    print("Print verification list:")
    print(verificationList)
