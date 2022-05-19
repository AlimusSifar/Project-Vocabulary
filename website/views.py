from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Word

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    data = {
        "words": Word.query.order_by(Word.word).all(),
    }
    return render_template('index.html', user=current_user, **data)


@views.route('/about', methods=['GET'])
def about():
    data = {}
    return '<h1>About</h1>'


@views.route('/profile', methods=['GET'])
@login_required
def profile():
    data = {}
    return '<h1>Profile</h1>'
