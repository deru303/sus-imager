FROM python:3.11-alpine
COPY . /opt/dc-imager
WORKDIR /opt/dc-imager
RUN python3 -m pip install -r requirements.txt

ENV DC_IMAGER_TOKEN ""
CMD ["python3", "main.py"]