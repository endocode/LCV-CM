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

license_list = ['MIT', 'Apache-2.0', 'GPL-2.0-only']

def CSV_to_dataframe(CSVfilePath, column_names_list):
    """
    Import a CSV and transform it into a pandas dataframe selecting only the useful columns from the Compatibility Matrix
    """
    df = pd.read_csv(CSVfilePath, usecols=column_names_list)
    return df


def Mapping(InboundLicenses_cleaned):
    CSVfilePath = "../../csv/spdx-id.csv"
    InboundLicenses_SPDX = []
    column_names_list = ['Scancode', 'SPDX-ID']
    df = CSV_to_dataframe(CSVfilePath, column_names_list)
    df = df.set_index('Scancode')
    for license in InboundLicenses_cleaned:
        newElement = df.loc[license]['SPDX-ID']
        if newElement is not np.nan:
            # print(newElement)
            InboundLicenses_SPDX.append(newElement)
            #if orLater in newElement:
                #print("The usage of 'or later' is not supported. \n Please specify a license version instead of using 'or later' notation.")
        else:
            InboundLicenses_SPDX.append(license)
        # print(InboundLicenses_cleaned)

    return InboundLicenses_SPDX


'''
#re approach
def SPDXMapping(license):
    for item in license_list:
        if re.match("mit$",item, flags=re.I): # re.I == re.IGNORECASE



#split approach
    list_of_words = license.split()
    if word in list_of_words:
'''
