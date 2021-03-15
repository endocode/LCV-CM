import urllib.request
import requests, json, time, sys
from verify import verify
from verify import SPDXIdMapping
from testlists import JSONPathList, GitHubURLList


orLater = "or-later"
JSONPath = JSONPathList()
GitHubURL = GitHubURLList()
index = 8
t = 10

def runtimer(t):
    print("tasks done, now sleeping for "+str(t)+" seconds")
    for i in range(t,0,-1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)

def retrieveOutboundLicense(url):
    response = requests.get(url).json()
    content = response['license']['spdx_id']
    if content == "NOASSERTION":
        print("SPDX ID's outbound license not correctly defined for the project: "+GitHubURL[index])
        print("Please use a project with an outbound license defined with its SPDX id")
        runtimer(t)

        #exit(0)
        #return
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


#for url in GitHubURL:
while index < len(GitHubURL):
    print("\n\nTest number "+str(index)+ " running\n\n ")
    url = GitHubURL[index]
    print(url)
    OutboundLicense = retrieveOutboundLicense(url)
    print(JSONPath[index])
    #print("Test number "+str(index)+" completed.")
    license_list = InboundLicenses(JSONPath[index])
    print(license_list)
    index += 1


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

        print(license_list_SPDX)
        print(OutboundLicense)
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

        runtimer(t)
        print("#################")
        print("##Running the next test .... ")
