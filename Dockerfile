FROM ubuntu:focal-20201106
RUN apt-get update -y && apt-get install -y python3-pip python-dev libpq-dev git curl npm
RUN npm install -g newman
RUN git clone https://github.com/endocode/LCV-CM.git
WORKDIR "/LCV-CM"
RUN make
EXPOSE 3251
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
