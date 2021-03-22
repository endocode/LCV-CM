from LCVlib.verify import retrieveOutboundLicense, compare, compareSPDX
import logging
import signal
import time
from dotenv import load_dotenv
from os import environ, path
import os
from flask import request, jsonify, render_template
import subprocess
from subprocess import check_output
import flask
import argparse
import sys

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
# API Shutdown function
PID = os.getpid()


def shutdown(secs):
    print("Shutting down server in:")
    for i in range(int(secs), 0, -1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)
    os.kill(int(PID), signal.SIGINT)


# Check the port number range
class PortAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 0 < values < 2**16:
            raise argparse.ArgumentError(
                self, "port numbers must be between 0 and 65535")
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port",
                    help='Port number to connect to',
                    dest='port',
                    # default=PORT,
                    type=int,
                    action=PortAction,
                    metavar="{0..65535}")
parser.add_argument("-P", "--PATH",
                    help='PATH environment override',
                    dest='PATH',
                    # default=environ.get('PYTHONHOME'),
                    type=str)
parser.add_argument("-s", "--shutdown",
                    help='shutdown timer express in seconds',
                    dest='shutdown',
                    # default="SHUTDOWN",
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
    hash = check_output(["git", "ls-remote", "-h", gitrepoName])
    hash = str(hash)
    hashOutput = hash.split()
    hashHead = hashOutput[0]
    hashHead = hashHead[3:42]
    return hashHead


app = flask.Flask(__name__)
app.config["DEBUG"] = False
logging.basicConfig(filename=LOGFILE, level=logging.INFO)


@app.route('/GitHubOutboundLicense')
def Outb():
    return render_template('outbound.html')


@app.route('/GitHubOutboundLicenseOutput', methods=['POST', 'GET'])
def GitHubOutboundLicense():
    if request.method == 'POST':
        url = request.form['nm']
        OutboundLicense = retrieveOutboundLicense(url)
        return OutboundLicense


@app.route('/Compatibility')
def Compatibility():
    return render_template('compatibility.html')


@app.route('/CompatibilityOutput', methods=['POST', 'GET'])
def Compliance():
    if request.method == 'POST':
        license_list = request.form['inboundLicenses']
        license_list = license_list.split(",")
        OutboundLicense = request.form['outboundLicense']
        verificationList = compare(license_list, OutboundLicense)
        #print(verificationList)
        return jsonify(verificationList)


@app.route('/CompatibilitySPDX')
def CompatibilitySPDX():
    return render_template('compatibilitySPDX.html')


@app.route('/CompatibilitySPDXOutput', methods=['POST', 'GET'])
def ComplianceSPDX():
    if request.method == 'POST':
        license_list = request.form['inboundLicenses']
        license_list = license_list.split(",")
        #print(license_list)
        OutboundLicense = request.form['outboundLicense']
        verificationList = compareSPDX(license_list, OutboundLicense)
        #print("Hello from ComplianceSPDX endpoint")
        #print(verificationList)
        return jsonify(verificationList)

# not strictly useful endpoints (at the moment)


@app.route('/versionz')
def version():
    GitHeadHash = GitHash(GITREPO)
    return jsonify(GitProject=GITREPO,
                   GitHeadHash=GitHeadHash)


@app.route('/shutdown/', defaults={"secs": "1"})
@app.route('/shutdown/<secs>')
def shutd(secs):
    shutdown(int(secs))
    return "Shutting down server"


@app.route('/PATH', methods=['GET'])
def path():
    CurrentPath = os.getenv("PATH")
    return str(CurrentPath)


f = open("serverParameters/PORT.txt", "w")
f.write(str(PORT))
f.close()
f = open("shutdown.txt", "w")
f.write("SHUTDOWN="+str(SHUTDOWN)+"\n")
f.close()
# PID = os.getpid()
f = open("shutdown.txt", "a")
f.write("PID="+str(PID))
f.close()

limit = -1
SHUTDOWN = int(SHUTDOWN)
if SHUTDOWN > limit:
    subprocess.Popen(["python3", "server_shutdown.py"])

app.run(host=HOST, port=PORT)