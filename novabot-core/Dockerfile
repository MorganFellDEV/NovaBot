FROM python:3

WORKDIR /usr/src/app
RUN mkdir -p /usr/src/app/novabot-resources

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./novabot_core.py" ]