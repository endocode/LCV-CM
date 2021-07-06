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

'''
* SPDX-FileCopyrightText: 2021 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: MIT
'''


license_list = ['The Apache Software License, Version 2.0', 'Apache License, Version 1.0']
#re approach

licenses = ["Apache","GPL"]
versions = ["1.0","2.0"]

def Re(licenses):
    for item in license_list:
        list_of_words = item.split()
        for license in licenses:
            #here should a control upon case sensitivity
            if license in list_of_words:
                for version in versions:
                    if version in list_of_words:
                        supposedLicenseSPDX = license+"-"+version
                        supposedLicense = license+" "+version
                        print("Supposed License: "+supposedLicense)
                        print("Supposed License SPDX: "+supposedLicenseSPDX)



        '''
        if re.match("Apache$",item, flags=re.I): # re.I == re.IGNORECASE
            print(item)
        '''

Re(licenses)

'''
my_list = ['webcam old', 'home', 'Space', 'Maybe later', 'Webcamnew']
for item in my_list:
    list_of_words = item.split()
    if word in list_of_words:
        if re.match("webcam$",item, flags=re.I): # re.I == re.IGNORECASE
            print(item)
'''

'''
CSVfilePath = "/home/michelescarlato/gitrepo/LCV-CM-Fasten/LCV-CM/csv/OSADL_transposed.csv"

# Outbound
column_names_list = ['MIT']
column_names_list.insert(0, 'License')
df = pd.read_csv(CSVfilePath, usecols=column_names_list)
print(df)
License = "Pippo"


Column_array = df.to_numpy()

#df.loc[:, 'License']
print(Column_array)
if (License in Column_array):
    print("License is in the Matrix")
else:
    print("License is not in the Matrix")
#df[~df.License.isin(License)]

#print(df)
#df.iloc[-1, -1] = "License"
#print(df)
'''
