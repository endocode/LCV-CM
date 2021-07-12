import sys
from LCVlib.testlistsGithubAPI import GitHubURLList
from LCVlib.testlistsJSONfiles import JSONPathList
#from LCVlib.verify import retrieveOutboundLicense, CheckOutboundLicense
#from LCVlib.verify import RetrieveInboundLicenses, Compare, CompareFlag
import requests
import json
import time
import sys
import pandas as pd
import numpy as np
import re
from LCVlib.SPDXIdMapping import StaticMappingList,IsASPDX,StaticMapping,DynamicMapping
from LCVlib.verify import CSV_to_dataframeOSADL

'''
* SPDX-FileCopyrightText: 2021 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: MIT
'''

df = CSV_to_dataframeOSADL("../../csv/OSADL.csv")
supported_licenses_OSADL = list(df.index)
#print(supported_licenses_OSADL)


license_list = ['AGPL 3.0 only','The Apache Software License, Version 2.0', 'Apache License, Version 1.0','AGPL 3.0 or later','GPL 3.0 only','MIT Licensed']
#re approach

# Currently the algorithm is not able to reason like: "General Public License = GPL"
# Artistic is artistic-1.0-perl, try to catch it!
# BSD contains the Clause word after the version number - which is not including .0 or .1
# bzip versions are in the format 1.0.5 or 1.0.6.
# still you are not catching classpath with this logic
# MIT CMU will be hardly recognized
# MPL no copyleft cannot be recognized with this method
# MS-PL (Microsoft Public License) and MS-RL (Microsoft Reciprocal License) cannot be recognized
# Unicode DFS 2015 and 2016 currently cannot be re-composed.
# zlib-acknowledgement can be matched only with hyphen in the middle, inasmuch zlib is written equally.
licenses = ["AFL","AGPL","Apache","Artistic","BSD","BSL","bzip2","CC0","CDDL","CPL","curl","EFL","EPL","EUPL","FTL","GPL","HPND","IBM","ICU","IJG","IPL","ISC",
"LGPL","Libpng","libtiff","MirOS","MIT","CMU","MPL","MS","NBPL","NTP","OpenSSL","OSL","Python","Qhull","RPL","SunPro","Unicode","UPL","WTFPL","X11","XFree86","Zlib","zlib-acknowledgement"]
versions = ["1.0","1.0.5","1.0.6","1.1","1.5","2.0","2.1","3.0","3.1"]

# To do: excluding the "," from parsing - currently it remains attached to the License, word e.g.

def DynamicMapping(verbose_license):
    #print(verbose_license)
    licenseVersion = None
    licenseName = None
    orLater=False
    only=False
    list_of_words = verbose_license.split()
    for word in list_of_words:
        if word in licenses:
            licenseName=word
        if word in versions:
            licenseVersion=word
        if word == "Later" or word == "later":
            print(word)
            orLater=True
        if word == "Only" or word == "only":
            print(word)
            only=True
    # after scanning the whole verbose license

    if licenseName is not None and licenseVersion is None:
        supposedLicenseSPDX = licenseName
        print("Supposed License SPDX: "+supposedLicenseSPDX)
        return supposedLicenseSPDX
    if not orLater and not only:
        print(orLater)
        print(only)
        if licenseName and licenseVersion is not None:
            supposedLicense = licenseName+" "+licenseVersion
            supposedLicenseSPDX = licenseName+"-"+licenseVersion
            print("Supposed License: "+supposedLicense)
            print("Supposed License SPDX: "+supposedLicenseSPDX)
            return supposedLicenseSPDX
    if orLater:
        print(orLater)
        if licenseName and licenseVersion is not None:
            supposedLicense = licenseName+" "+licenseVersion+" or later"
            supposedLicenseSPDX = licenseName+"-"+licenseVersion+"-or-later"
            print("Supposed License: "+supposedLicense)
            print("Supposed License SPDX: "+supposedLicenseSPDX)
            return supposedLicenseSPDX
    if only:
        print(only)
        if licenseName and licenseVersion is not None:
            supposedLicense = licenseName+" "+licenseVersion+" only"
            supposedLicenseSPDX = licenseName+"-"+licenseVersion+"-only"
            print("Supposed License: "+supposedLicense)
            print("Supposed License SPDX: "+supposedLicenseSPDX)
            return supposedLicenseSPDX

DM_license_list=[]
DM_license_list_to_Map=[]
DM_license_list_SPDX=[]
# for inbound licenses or just CheckOutboundLicense
for verbose_license in license_list:
    print(verbose_license)
    license = StaticMapping(verbose_license)
    #print(license)
    # this check has no sense.
    # here is going to end up or the SPDX-id, or the verbose_license name.
    #if license is not None:

    # IF ... IS An SPDX ID
    IsASPDX(license)

    # IF IT IS NOT:
    # run DynamicMapping


    #DM_license_list.append(license)


'''
print("Printing list afther Re")
print(DM_license_list)

for license in DM_license_list:
    if license in supported_licenses_OSADL:
        #print(license)
        print(license+" is an SDPX id")
        DM_license_list_SPDX.append(license)
    else:
        #Mapping(DM_license_list)
        print(license+" is NOT an SDPX id")
        DM_license_list_to_Map.append(license)

DM_license_list_Mapped=StaticMappingList(DM_license_list_to_Map)
print(DM_license_list_Mapped)

final_SPDX_ID_list = DM_license_list_SPDX + DM_license_list_Mapped
print(final_SPDX_ID_list)
'''
