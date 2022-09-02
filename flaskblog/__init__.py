# we initialise our application and bring together different components
# this file tells python that this is apackage
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # relative path,this file will be created in our proj dir
db = SQLAlchemy(app)  # initialising sqlalchemy database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)  # we add functionality to db models, and it will handle all sessions in background
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'  # boostrap class for nicely colored info alert

from flaskblog import routes  # when we run our application, it can find routes
