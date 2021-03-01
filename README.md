# License Compliance Validator (LCV) and Compatibility Matrix (CM)

This is the Python version of [GO-LCV](https://github.com/endocode/GO-LCV).
LCV takes input a json generated by the QMSTR JSON Reporter and analyzes all its licenses.

The Compatibility Matrix (CM) will match these licenses. The CM is represented in the `license.csv` file.
The Python version is currently giving as output what inbound licenses are not compatible with each other, considering the compatibility's directionality.
E.g., Source code released under Apache 2.0 license can be used within a project released under the GPL3.0 license, but not vice-versa. 

It is still missing the comparison of inbound licenses against the outbound license.
Currently, the code is taking in input all the inbound licenses and compare them with each other. An approach that could be useful to highlight under which license the whole project could be released.
