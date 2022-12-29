FROM python:3.10.4-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --upgrade pip \
    pip install pyTelegramBotAPI \
    pip install pytelegrambotapi --upgrade 


CMD [ "python", "main.py" ]