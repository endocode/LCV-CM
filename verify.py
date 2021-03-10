#!/usr/bin/python
import psycopg2
import pandas as pd
import numpy as np

from config import config
orLater = "or-later"

def CSV_to_dataframe(CSVfilePath, column_names_list):
    """
    Import a CSV and transform it into a pandas dataframe
    """
    df = pd.read_csv (CSVfilePath, usecols=column_names_list)

    return df


def SPDXIdMapping(license_list_cleaned):
    CSVfilePath = "spdx-id.csv"
    license_list_SPDX = []
    column_names_list = ['Scancode','SPDX-ID']
    df = CSV_to_dataframe(CSVfilePath, column_names_list)
    df = df.set_index('Scancode')
    for license in license_list_cleaned:
        newElement=df.loc[license]['SPDX-ID']
        if newElement is not np.nan:
            license_list_SPDX.append(newElement)
            if orLater in newElement:
                print("The usage of 'or later' is not supported. \n Please specify a license version instead of using 'or later' notation.")
                exit(0)
        else:
            license_list_SPDX.append(license)
    return license_list_SPDX


def verify(license_list_cleaned, OutboundLicense):
    CSVfilePath = "licenses.csv"
    column_names_list = [OutboundLicense]
    column_names_list.insert(0,'License')

    # retrieve data from CSV file
    df = CSV_to_dataframe(CSVfilePath, column_names_list)
    df = df.set_index('License')
    if (len(license_list_cleaned)==1) and (license_list_cleaned[0]==OutboundLicense):
        print("For this project only "+license_list_cleaned[0]+" as the inbound license has been detected, and it is the same of the outbound license ("+OutboundLicense+"). \nIt means that it is license compliant. ")
        exit(0)

    verificationList = list()
    for license in license_list_cleaned:
        comparison = df.loc[license, OutboundLicense]
        if comparison == "0" :
            output = license+" is not compatible with "+OutboundLicense+" as an outbound license."
            verificationList.append(output)
        else:
            output = license+" is compatible with "+OutboundLicense+ " as an outbound license."
            verificationList.append(output)
    return verificationList
