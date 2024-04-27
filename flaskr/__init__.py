import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    load_dotenv()
    if os.getenv('FLASK_ENV') == 'development':
        app.config.from_object('flaskr.config.DevelopmentConfig')
    else :
        app.config.from_object('flaskr.config.Config')

    if test_config is not None:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .db import db
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

    from flaskr.routes import routes
    app.register_blueprint(routes, url_prefix='/api')

    return app