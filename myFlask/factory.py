from flask import Flask
from flask_cors import CORS, cross_origin
from myFlask import envconfig
import os 
from .celeryUtils import initCelery


PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]



def create_app(appName=PKG_NAME, **kwargs):
    flask_app = Flask(appName)

    if kwargs.get("celery"):
    	initCelery(kwargs.get("celery"), flask_app)
    cors = CORS(flask_app)
    return flask_app
    
# app = create_app()


# cwd = os.getcwd()
# app = Flask(__name__)
# cors = CORS(app)
# app.config['CELERY_BROKER_URL'] = 'rbmq://localhost:5672'
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['UPLOAD_FOLDER'] = os.path.join(cwd, 'upload')
# # app.config.from_object(envconfig.DevelopmentConfig)
# app.secret_key = 'super secret key'



