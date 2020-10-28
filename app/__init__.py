from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

print('{} is using me'.format(__name__))

from app import routes