FROM ubuntu:22.04 
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y python3.12 mpg123 python3-pip libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev && pip3 install -r requirements.txt
CMD ["python3", "main.py"]