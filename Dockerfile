FROM ubuntu

ADD ./ ./

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install -r requirements.txt

CMD ["python3","server.py"]