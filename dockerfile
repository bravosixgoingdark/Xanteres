FROM ubuntu:22.04 
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install -r requirements.txt
CMD ["python3", "main.py"]
```