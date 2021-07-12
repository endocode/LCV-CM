#!/usr/bin/python
# import urllib.request
import requests
import json
import time
import sys
import pandas as pd
import numpy as np
import re
import csv

'''
* SPDX-FileCopyrightText: 2021 Michele Scarlato <michele.scarlato@endocode.com>
*
* SPDX-License-Identifier: MIT
'''

licenses = ["AFL","AGPL","Apache","Artistic","BSD","BSL","bzip2","CC0","CDDL","CPL","curl","EFL","EPL","EUPL","FTL","GPL","HPND","IBM","ICU","IJG","IPL","ISC",
"LGPL","Libpng","libtiff","MirOS","MIT","CMU","MPL","MS","NBPL","NTP","OpenSSL","OSL","Python","Qhull","RPL","SunPro","Unicode","UPL","WTFPL","X11","XFree86","Zlib","zlib-acknowledgement"]
versions = ["1.0","1.0.5","1.0.6","1.1","1.5","2.0","2.1","3.0","3.1"]


def CSV_to_dataframe(CSVfilePath, column_names_list):
    """
    Import a CSV and transform it into a pandas dataframe selecting only the useful columns from the Compatibility Matrix
    """
    df = pd.read_csv(CSVfilePath, usecols=column_names_list)
    return df


def StaticMapping(single_verbose_license):
    #print(single_verbose_license)
    #1540 entries
    CSVfilePath = "../../csv/spdx-id.csv"
    #InboundLicenses_SPDX = []
    column_names_list = ['Scancode', 'SPDX-ID']
    df = CSV_to_dataframe(CSVfilePath, column_names_list)
    print(df)
    df = df.set_index('Scancode')
    # @Michele you should insert a check upon the column of "scancode name", if the license is there, enter the cycle
    # if not, provide an output without producing a KeyError
    #for license in InboundLicenses_cleaned:
    single_verbose_license_SPDX_id = df.loc[single_verbose_license]['SPDX-ID']
    print(single_verbose_license_SPDX_id)
    if single_verbose_license_SPDX_id is not np.nan:
        #InboundLicenses_SPDX.append(newElement)
        return single_verbose_license_SPDX_id
    else:
        #InboundLicenses_SPDX.append(license)
        return single_verbose_license

def IsASPDX(license_name):
    with open('../../csv/SPDX_license_name.csv', 'rt') as f:
         reader = csv.reader(f)
         for row in reader:
              for field in row:
                  if field == license_name:
                      print(license_name+"is a SPDX-id")

def StaticMappingList(InboundLicenses_cleaned):
    print(InboundLicenses_cleaned)
    CSVfilePath = "../../csv/spdx-id.csv"
    InboundLicenses_SPDX = []
    column_names_list = ['Scancode', 'SPDX-ID']
    df = CSV_to_dataframe(CSVfilePath, column_names_list)
    df = df.set_index('Scancode')
    # @Michele you should insert a check upon the column of "scancode name", if the license is there, enter the cycle
    # if not, provide an output without producing a KeyError
    for license in InboundLicenses_cleaned:
        newElement = df.loc[license]['SPDX-ID']
        if newElement is not np.nan:
            InboundLicenses_SPDX.append(newElement)
        else:
            InboundLicenses_SPDX.append(license)
    return InboundLicenses_SPDX

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




# possible inputs from Maven central
#license_list = ['The Apache Software License, Version 2.0', 'Apache License, Version 2.0']

# possible licenses keywords
#licenses = ["Apache","GPL"]
# possible versions list
#versions = ["1.0","2.0"]

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
#split approach
    list_of_words = license.split()
    if word in list_of_words:
'''
