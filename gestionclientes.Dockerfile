FROM python:3.10

EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir "pip<24.1" setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=src/gestionclientes/api

CMD ["flask", "--debug", "run", "--host=0.0.0.0", "--port=5000"]
