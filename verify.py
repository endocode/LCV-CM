#!/usr/bin/python
import urllib.request
import requests, json, time, sys
import psycopg2
import pandas as pd
import numpy as np

from config import config
orLater = "or-later"

def CSV_to_dataframe(CSVfilePath, column_names_list):
    """
    Import a CSV and transform it into a pandas dataframe selecting only the useful columns from the Compatibility Matrix
    """
    df = pd.read_csv (CSVfilePath, usecols=column_names_list)

    return df

def retrieveOutboundLicense(url):
    response = requests.get(url).json()
    content = response['license']['spdx_id']
    if content == "NOASSERTION":
        print(content)
        print("Outbound noassertion")
    return content

def InboundLicenses(JSONPath):
    print("Started Reading JSON report")
    with open(JSONPath, "r") as read_file:
        print("Reading: " + JSONPath)
        data = json.load(read_file)#dict
        license_list = []
        for i in data['payload']['fileMetadata']:
            for x in (i['licenses']):
                if not x in license_list:
                    license_list.append(x)
    print("Finished reading JSON report")
    print("###################")
    return license_list


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
                #exit(0)
        else:
            license_list_SPDX.append(license)
    return license_list_SPDX


def verify(CSVfilePath,license_list_cleaned, OutboundLicense):
    # CSVfilePath = "licenses.csv"
    column_names_list = [OutboundLicense]
    column_names_list.insert(0,'License')
    verificationList = list()
    # retrieve data from CSV file
    df = CSV_to_dataframe(CSVfilePath, column_names_list)
    df = df.set_index('License')
    if (len(license_list_cleaned)==1) and (license_list_cleaned[0]==OutboundLicense):
        output = "For this project only "+license_list_cleaned[0]+" as the inbound license has been detected, and it is the same of the outbound license ("+OutboundLicense+"), implying that it is compatible. \nIt means that it is license compliant. "
        verificationList.append(output)
        return verificationList

    for license in license_list_cleaned:
        comparison = df.loc[license, OutboundLicense]
        if comparison == "0" :
            output = license+" is not compatible with "+OutboundLicense+" as an outbound license."
            verificationList.append(output)
        if comparison == "NS" :
            output = license+" is not supported, because 'or later' notation."
            verificationList.append(output)
        if comparison == "1":
            output = license+" is compatible with "+OutboundLicense+ " as an outbound license."
            verificationList.append(output)
        if comparison == "TBD":
            output = license+" compatibility with "+OutboundLicense+ " still needs to be defined."
            verificationList.append(output)
        if comparison == "UNK":
            output = "An UNKNOWN license has been found within the project. This cannot reveal license incompatibility"
            verificationList.append(output)
    return verificationList


def compare(license_list,OutboundLicense):
    if OutboundLicense != "NOASSERTION":
        print("The outbound license for the project is: "+OutboundLicense)

        if orLater in OutboundLicense:
            print("The usage of `'or later' is not supported. \n Please specify a license version instead of using `'or later'` notation.")
            exit(0)

        if len(license_list)==1:
            print("The only inbound license detected is:")
            print(license_list[0])
        else:
            print("The inbound licenses found are:")
            print(license_list)

        license_list_SPDX = SPDXIdMapping(license_list)

        if len(license_list_SPDX)==1:
            print("The SPDX id for the only inbound license detected is:")
            print(license_list_SPDX[0])
        else:
            print("The SPDX IDs for the inbound licenses found are:")
            print(license_list_SPDX)


        print("#################")
        print("Running the license compliance verification:")

        print("Inbound license list :\n"+str(license_list_SPDX))
        print("The outbound license is :"+OutboundLicense)
        #verify(license_list_SPDX, OutboundLicense)
        CSVfilePath = "licenses_tests.csv"
        verificationList = verify(CSVfilePath,license_list_SPDX, OutboundLicense)

        notCompatible = "is not compatible"
        Compatible = "is compatible"
        isNotSupported = "is not supported"
        TBD = "compatibility with"
        UNK = "UNKNOWN"
        for element in verificationList:
            if notCompatible in element:
                print("YOUR PACKAGE IS NOT COMPLIANT because:\n"+element)
            if Compatible in element:
                print("\n"+element+"\nThis allow you to use this inbound license in your package.\n")
            if isNotSupported in element:
                print("\n"+element+"\nMomentairly 'or later' notation are not supported.\n")
            if TBD in element:
                print("\n"+element+"\nThis compatibility association still need to be defined.\n")
            if UNK in element:
                print("\n"+element)
        #if all element are compatible, license compliance occurs.
        indexLicense = 0
        for element in verificationList:
            if Compatible in element:
                indexLicense+=1
        print(str(indexLicense)+" above "+str(len(verificationList))+" licenses found are compatible.")
        if indexLicense == len(verificationList):
            print("Hence your project is compatible.")
        else:
            print("Hence your project is not compatible.")
    else:
        print("This project does not specify correctly an SPDX id for its oubound license")

def runtimer(t):
    print("###############################################")
    print("tasks done, now sleeping for "+str(t)+" seconds")
    for i in range(t,0,-1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)
    print("\n")
