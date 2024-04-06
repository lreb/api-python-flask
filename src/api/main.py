from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from endpoints.index import welcome_api
from endpoints.demo import demo_api
from endpoints.auth import auth_api
from models.model import db, Demo

#import jwt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://chinoadmin:Pa$$word1987@localhost:5432/local_development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://127.0.0.1:105/static/swagger.json'  # Our API url (can be local)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be served at {SWAGGER_URL}/dist/
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(welcome_api, url_prefix='/api/welcome')
app.register_blueprint(demo_api, url_prefix='/api/demo')
app.register_blueprint(auth_api, url_prefix='/api/auth')


if __name__ == '__main__':
    app.debug = True
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=105)
