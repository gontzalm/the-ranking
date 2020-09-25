FROM ubuntu

COPY . .

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install -r docker/requirements.txt

CMD [ "python3", "server.py" ]