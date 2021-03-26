import sys
from LCVlib.testlistsGithubAPI import GitHubURLList
from LCVlib.testlistsJSONfiles import JSONPathList
from LCVlib.verify import retrieveOutboundLicense, CheckOutboundLicense
from LCVlib.verify import RetrieveInboundLicenses, Compare
'''
* SPDX-FileCopyrightText: 2021 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: MIT
'''


JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
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
    InboundLicenses = RetrieveInboundLicenses(JSON)
    verificationList = Compare(InboundLicenses, OutboundLicense)
    print("Print verification list:")
    print(verificationList)
