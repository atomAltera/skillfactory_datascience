FROM python:3.7-buster


WORKDIR /tmp
ADD ./requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /opt

VOLUME /opt
EXPOSE 8888


CMD jupyter notebook --port 8888 --ip=0.0.0.0 --allow-root
