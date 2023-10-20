FROM python:3.10-slim-buster
COPY . /delete-security-auditlog
WORKDIR /delete-security-auditlog
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]