import logging
import sys
import argparse
import urllib
import flask
import re
from subprocess import check_output
import subprocess
from json import dumps
from flask import Flask, redirect, url_for, request, current_app, Blueprint, jsonify, render_template
import os
#App configuration
from os import environ, path, system
from dotenv import load_dotenv
import time
import json, os, signal
#   sys.path.append('~/gitrepo/LCV-CM/LCVlib')
sys.path.append('..')
import LCVlib.verify


import urllib.request
import requests, json, time, sys
import psycopg2
import pandas as pd
import numpy as np

# Load .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
# Load parametrs from .env file
PATH = environ.get('PATH')
LOGFILE = environ.get('LOGFILE')
PORT = environ.get('PORT')
HOST = environ.get('HOST')
GITREPO = environ.get('GITREPO')
SHUTDOWN = environ.get('SHUTDOWN')

def retrieveOutboundLicense(url):
    print("Retrieving outbound license from: "+url)
    response = requests.get(url).json()
    content = response['license']['spdx_id']
    if content == "NOASSERTION":
        print(content)
        print("Outbound noassertion")
    else:
        print("Outbound license: "+content)
    return content

#API Shutdown function
PID = os.getpid()
def shutdown(secs):
    print("Shutting down server in:")
    for i in range(int(secs),0,-1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)
    os.kill(int(PID), signal.SIGINT)
# This fixed a visualization error in the browser


#Check the port number range
class PortAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 0 < values < 2**16:
            raise argparse.ArgumentError(self, "port numbers must be between 0 and 65535")
        setattr(namespace, self.dest, values)
parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port",
                        help='Port number to connect to',
                        dest='port',
                        #default=PORT,
                        type=int,
                        action=PortAction,
                        metavar="{0..65535}")
parser.add_argument("-P", "--PATH",
                        help='PATH environment override',
                        dest='PATH',
                        #default=environ.get('PYTHONHOME'),
                        type=str)
parser.add_argument("-s", "--shutdown",
                        help='shutdown timer express in seconds',
                        dest='shutdown',
                        #default="SHUTDOWN",
                        type=str)


args = parser.parse_args()

if args.port:
    PORT = args.port
if args.PATH:
    PATH = args.PATH
if args.shutdown:
    SHUTDOWN = args.shutdown
os.environ['PATH'] = PATH


# Git hash of the head of the repository
def GitHash(gitrepoName):
    hash = check_output(["git", "ls-remote","-h", gitrepoName])
    hash = str(hash)
    hashOutput = hash.split()
    hashHead = hashOutput[0]
    hashHead = hashHead[3:42]
    return hashHead

app = flask.Flask(__name__)
app.config["DEBUG"] = False
logging.basicConfig(filename=LOGFILE, level=logging.INFO)


@app.route('/versionz')
def version():
    GitHeadHash= GitHash(GITREPO)
    return jsonify(GitProject = GITREPO,
                    GitHeadHash= GitHeadHash)

@app.route('/shutdown/', defaults={"secs":"1"})
@app.route('/shutdown/<secs>')
def shutd(secs):
    shutdown(int(secs))
    return "Shutting down server"

@app.route('/PATH', methods=['GET'])
def path():
    CurrentPath = os.getenv("PATH")
    return str(CurrentPath)


@app.route('/GetOutboundLicenseTest/')
def GetOutboundLicenseTest():
    url="https://api.github.com/repos/hope-for/hope-boot/license"
    OutboundLicense=retrieveOutboundLicense(url)
    return OutboundLicense

@app.route('/GitHubOutboundLicense')
def Outb():
   return render_template('outbound.html')

@app.route('/GitHubOutboundLicenseOutput',methods = ['POST', 'GET'])
def GitHubOutboundLicense():
    if request.method == 'POST':
        url = request.form['nm']
        OutboundLicense=retrieveOutboundLicense(url)
        return OutboundLicense
#NOT FUNCTIONING ENDPOINTS
@app.route('/GetOutboundLicense/<url>')
def GetOutboundLicense(url="https://api.github.com/repos/hope-for/hope-boot/license"):
    #url="https://api.github.com/repos/hope-for/hope-boot/license"
    OutboundLicense=retrieveOutboundLicense(url)
    return OutboundLicense

f = open("tests/PORT.txt", "w")
f.write(str(PORT))
f.close()
f = open("shutdown.txt", "w")
f.write("SHUTDOWN="+str(SHUTDOWN)+"\n")
f.close()
#PID = os.getpid()
f = open("shutdown.txt", "a")
f.write("PID="+str(PID))
f.close()

limit = -1
SHUTDOWN = int(SHUTDOWN)
if SHUTDOWN > limit:
    subprocess.Popen(["python3", "server_shutdown.py"])

app.run(host=HOST, port=PORT)
