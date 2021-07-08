#!/usr/bin/python
# import urllib.request
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

def CSV_to_dataframe(CSVfilePath, column_names_list):
    """
    Import a CSV and transform it into a pandas dataframe selecting only the useful columns from the Compatibility Matrix
    """
    df = pd.read_csv(CSVfilePath, usecols=column_names_list)
    return df


def Mapping(InboundLicenses_cleaned):
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


# possible inputs from Maven central
license_list = ['The Apache Software License, Version 2.0', 'Apache License, Version 2.0']

# possible licenses keywords
licenses = ["Apache","GPL"]
# possible versions list
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
#split approach
    list_of_words = license.split()
    if word in list_of_words:
'''
