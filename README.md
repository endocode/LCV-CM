# License Compliance Verifier (LCV) and Compatibility Matrix (CM)

This is the Python version of [GO-LCV](https://github.com/endocode/GO-LCV).
LCV takes input a json generated by the QMSTR JSON Reporter and analyzes all its licenses.

The Compatibility Matrix (CM) will match these licenses. The CM is represented in the `license.csv` file.
The Python version is currently giving as output what inbound licenses are not compatible with each other, considering the compatibility's directionality.
E.g., Source code released under Apache 2.0 license can be used within a project released under the GPL3.0 license, but not vice-versa.

It is still missing the comparison of inbound licenses against the outbound license.
Currently, the code is taking in input all the inbound licenses and compare them with each other. An approach that could be useful to highlight under which license the whole project could be released.

## How to run it:
The `json/` directory hosts a few JSON files generated by `QMSTR`.
The `main.py`, at line 6, is opening one of those files to extract the licenses found by `QMSTR`.
Before running the code, these dependencies are required:
```
pip3 install psycopg2
pip3 install pandas

```
Since the original idea was to create a Postgres table, instead of using a csv, also the library `libpq-dev` is a dependency.

To run the code with python3:
```
python3 main.py  
```

## How does the Matrix function
The rows represent `inbound` licenses and the columns `outbound` licenses.

The compatibility matrix functions in this way:
`QMSTR` will generate an array of licenses used within a project.
`LCV` can retrieve the outbound license for a given GitHub project through GitHub APIs.
The array elements will be matched against the outbound license declared for that specific project.

[https://github.com/endocode/LCV-CM/blob/main/licenses.csv](https://github.com/endocode/LCV-CM/blob/main/licenses.csv) represents *True* with *1* and *False* with *0*, because originally this Matrix was thought to be imported as a Postgres table, that makes use of bit data to represent them.

## Acronyms used within the Matrix :

TBD = To be defined: associations that still need to be defined.

NS = Not Supported: momentarily referred to the `or later` notations used for certain licenses.
Currently, LCV is supporting only specific licenses.


## Running it with Docker:
LCVServer.py implements the APIs to interact with the LCV algorithm that is performing License Compliance.
While using Main.py and Tests.py the LCV algorithm is collecting a single instance of each inbound license found in a given JSON (so far is accepting the QMSTR JSON Output, and can be easily adapted to the Scancode JSON Output), the APIs require to insert a list of inbound licenses, and the outbound license declared for a given project.
Given these two inputs, the LCV algorithm is able to perform the verification.
To build the APIS
Build the docker image locally:
```
docker build -t lcv-cm .
```
or
```
docker build --no-cache -t lcv-cm .
```
To avoid Docker build from using cache. The dockerfile clones this repository, so if it is required to update the docker image with code added recently, `--no-cache` would be the right option to apply the changes.

Running it:
```
docker run -it -p 8080:8080 lcv-cm
```
The LCVServer will run at the 8080 port of your localhost and can be reached via `http://0.0.0.0:8080/APIEndpoints` (WIP).
