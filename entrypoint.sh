#!/bin/sh -l

echo "Hello world"
cd /github/workspace/src/LCV
python3 LCVServer.py &
#newman run https://www.getpostman.com/collections/3b2724fe658897b87a57
newman run https://www.getpostman.com/collections/795fdf2c5c8f16cb82d8
