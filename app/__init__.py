from flask import Flask
app = Flask(__name__)

print('{} is using me'.format(__name__))

from app import routes