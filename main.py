from myFlask import factory
import myFlask
from myFlask.routes import init_app


app = factory.create_app(celery=myFlask.celery)
# app.run(debug=True, host='0.0.0.0') -> Doesn't need this line with gunicorn
init_app(app)
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
