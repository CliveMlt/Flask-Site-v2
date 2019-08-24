FROM python:3.7

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./file_server.py" ]