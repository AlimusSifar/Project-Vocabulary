import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from colorama import init, Fore
init(autoreset=True)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('my-app-key')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB_NAME = "vocabs"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///static/{DB_NAME}.db"
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")
    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")
    from .forms import forms
    app.register_blueprint(forms, url_prefix="/form")

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    create_sqlite_db(app, DB_NAME)

    @login_manager.user_loader
    def load_user(email):
        return User.query.get(email)
    return app


def create_sqlite_db(app, db_name):
    if not os.path.exists(f"website/static/{db_name}.db"):
        print(f"{Fore.YELLOW}Creating database {db_name}...")
        db.create_all(app=app)
        print(f"{Fore.GREEN}Database {db_name} created!")
