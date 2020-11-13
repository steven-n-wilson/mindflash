FROM python:3.7.6

WORKDIR /user/src/app

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY . . 

ENTRYPOINT ["python", "MindFlash.py"]