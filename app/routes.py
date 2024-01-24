from flask import render_template, url_for, flash, redirect, request, session
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

@app.route('/questionnaire', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/questionnaire/<int:page>', methods=['GET', 'POST'])
def questionnaire(page):
    per_page = 10
    total_questions = Question.query.count()
    total_pages = total_questions // per_page + (1 if total_questions % per_page > 0 else 0)

    if request.method == 'POST':
        # Menyimpan jawaban dari halaman saat ini ke sesi
        for key in request.form:
            session[key] = request.form[key]
        # Redirect ke halaman selanjutnya
        next_page = page + 1
        if next_page <= total_pages:
            return redirect(url_for('questionnaire', page=next_page))

    # Perbaikan di baris ini
    questions = Question.query.order_by(Question.id).paginate(page=page, per_page=per_page, error_out=False).items

    return render_template('questionnaire.html', questions=questions, page=page, total_pages=total_pages)

@app.route('/submit-test', methods=['POST'])
def submit_test():
    all_responses = {key: value for key, value in session.items() if key.startswith('question_')}
    # Proses jawaban untuk menyimpan ke database
    # ...
    # Kosongkan sesi setelah jawaban diproses
    session.clear()
    return redirect(url_for('result_page'))  # Asumsi ada route untuk menampilkan hasil
