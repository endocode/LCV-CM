FROM ubuntu:focal-20201106
RUN apt-get update -y && apt-get install -y python3-pip python-dev git curl
RUN git clone https://github.com/endocode/LCV-CM.git
WORKDIR "/LCV-CM/src/LCV"
RUN make
EXPOSE 8080
CMD ["python3","LCVServer.py"]
#RUN python3 server.py
