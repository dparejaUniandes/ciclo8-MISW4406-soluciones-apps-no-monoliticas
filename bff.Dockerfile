FROM python:3.10

EXPOSE 8003/tcp

COPY bff-requirements.txt ./
RUN pip install --no-cache-dir -r bff-requirements.txt

COPY . .

WORKDIR "/src"

CMD [ "uvicorn", "bff_web.main:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]