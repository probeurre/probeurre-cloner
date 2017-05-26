FROM python:3

VOLUME /probeurre-data

RUN apt-get update && \
    apt-get install -y git python3-pip
	
COPY probeurre.py /probeurre/probeurre.py
COPY requirements.txt /probeurre/requirements.txt

RUN pip3 install -r /probeurre/requirements.txt

ENTRYPOINT ["/probeurre/probeurre.py"]
