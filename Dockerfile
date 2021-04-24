FROM ubuntu:focal-20201106
RUN apt-get update -y && apt-get install -y python3-pip python-dev libpq-dev git curl
RUN git clone https://github.com/endocode/LCV-CM.git
#WORKDIR "/LCV-CM"
RUN make
#WORKDIR "/home/runner/work/LCV-CM/LCV-CM/src/LCV"
EXPOSE 3251
CMD ["cd","/home/runner/work/LCV-CM/LCV-CM/src/LCV"]
CMD ["python3","LCVServer.py"]
