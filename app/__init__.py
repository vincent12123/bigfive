from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_migrate import Migrate

app = Flask(__name__)
ckeditor = CKEditor(app)

app.config['UPLOAD_FOLDER'] = 'app/static'  # Gantilah dengan lokasi penyimpanan yang sesuai
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bigfive.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


from app import routes
