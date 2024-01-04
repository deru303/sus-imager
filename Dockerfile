FROM python:3.11-alpine
COPY . /opt/dc-imager
WORKDIR /opt/dc-imager
RUN python3 -m pip install -r bot/requirements.txt

ENV DC_IMAGER_TOKEN ""
CMD ["python3", "bot/main.py"]