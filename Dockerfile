FROM python:3.6

RUN pip install bottle

ADD web-server.py /web-server.py

EXPOSE 8000
CMD ["python", "/web-server.py"]