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


#re approach
def SPDXMapping(license):
    for item in license_list:
        if re.match("mit$",item, flags=re.I): # re.I == re.IGNORECASE
            


#split approach
    list_of_words = license.split()
    if word in list_of_words:
