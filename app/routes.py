from flask import render_template, url_for, flash, redirect, request
from app import app, db, login_manager
from app.models import Book, User, Dimension, Question
#from flask_login import login_user, current_user, logout_user, login_required


import os
from werkzeug.utils import secure_filename

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    #books = Book.query.all()
    return render_template('index.html')

@app.route('/question')
def question():
    #books = Book.query.all()
    return render_template('form.html')