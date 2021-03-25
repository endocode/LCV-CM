FROM ubuntu:focal-20201106
RUN apt-get update -y && apt-get install -y python3-pip python-dev libpq-dev git curl
RUN git clone https://github.com/endocode/LCV-CM.git
WORKDIR "/LCV-CM"
RUN make
WORKDIR "/LCV-CM/src/LCV"
EXPOSE 8080
CMD ["python3","LCVServer.py"]
# cd ~/gitrepo/LCV-CM/
# docker build -t lcv-cm .
# docker run -it -p 8080:8080 lcv-cm
