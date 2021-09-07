# from app.factory import create_app
import pymongo
import mysql.connector
from flask import jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import time
from myFlask.rbmq.receive import rec
from myFlask.rbmq.send import send

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'md'}



def init_app(app):
    @app.route('/')
    def index():
        return jsonify({"status": "OK", "msg":"server alive and running."})

    @app.route('/a')
    @cross_origin()
    def a():
        return jsonify({"status": "OK", "msg":"server alive and running."})

    @app.route('/upload', methods=['GET', 'POST'])
    @cross_origin()
    def upload_file():
        def allowed_file(filename):
            return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # mkdir if folder not exists
                if not os.path.exists(app.config['UPLOAD_FOLDER']):
                    os.makedirs(app.config['UPLOAD_FOLDER'])
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # redirect app to the URL where the 'upload_file' is declared
                print('uploaded {} to {}'.format(filename, os.path.join(app.config['UPLOAD_FOLDER'], filename)))
                return redirect(url_for('upload_file', filename=filename))
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''

    @app.route('/sleep')
    @cross_origin()
    def doSleep():
        print("Sleeping...")
        time.sleep(5)
        return "I'm awake!"


    @app.route('/gmsg')
    @cross_origin()
    def gmsg():
        if request.method == 'GET':
            rec()
        return "gmsg page"


    @app.route('/send', methods=['GET', 'POST'])
    @cross_origin()
    def sendmsg():
        if request.method == 'POST':
            tosend = request.form.get('tosend') 
            my_background_task.delay(tosend)
            return redirect(url_for('sendmsg'))

        return '''
        <!doctype html>
        <title>Send a message</title>
        <h1>Send a message</h1>
        <form method=post enctype=application/x-www-form-urlencoded>
          <input type=text name=tosend>
          <input type=submit value=Upload>
        </form>
        '''
