from celery import Celery 


def makeCelery(appName=__name__):
	return Celery('tasks', broker='amqp://localhost', backend='db+sqlite:///db.sqlite3')
celery = makeCelery()




# from flask import Flask
# from flask_cors import CORS, cross_origin
# from app import envconfig
# import os 



# def create_app():
#     flask_app = Flask(__name__)
#     return flask_app
    
# app = create_app()


# cwd = os.getcwd()
# app = Flask(__name__)
# cors = CORS(app)
# app.config['CELERY_BROKER_URL'] = 'rbmq://localhost:5672'
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['UPLOAD_FOLDER'] = os.path.join(cwd, 'upload')
# # app.config.from_object(envconfig.DevelopmentConfig)
# app.secret_key = 'super secret key'


from myFlask import routes
