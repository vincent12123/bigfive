from flask import render_template, url_for, flash, redirect, request
from app import app, db, login_manager
from app.models import  User, Question, Response, Result
from flask_login import login_user, current_user, logout_user, login_required
import random

import os
from werkzeug.utils import secure_filename

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    #books = Book.query.all()
    return render_template('index.html')

def get_questions():
    # Mengambil semua pertanyaan dari database
    questions = Question.query.all()
    return questions

@app.route('/questionnaire')
def questionnaire():
    questions = get_questions()
    random_questions = random.sample(questions, min(len(questions), 10))  # mengambil 10 pertanyaan secara acak, atau kurang jika tidak ada cukup pertanyaan
    return render_template('questionnaire.html', questions=random_questions)


