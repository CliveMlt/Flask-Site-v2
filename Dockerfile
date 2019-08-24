FROM python:3.7

WORKDIR /flask-file-server-5-hosting

COPY requirements.txt /flask-file-server-5-hosting/

COPY file_server.py /flask-file-server-5-hosting/

COPY static/* /flask-file-server-5-hosting/assets/

COPY templates/* /flask-file-server-5-hosting/templates/

RUN pip install -r requirements.txt

EXPOSE 8080


CMD [ "python", "./file_server.py" ]
