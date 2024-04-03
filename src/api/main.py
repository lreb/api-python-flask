from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from endpoints.index import welcome_api
from endpoints.demo import demo_api

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
