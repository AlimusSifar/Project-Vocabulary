from flask import Blueprint, request, redirect, flash
from flask_login import login_user, logout_user, login_required

from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def register():
    data = {
        "username": request.form.get('username'),
        "email": request.form.get('email'),
    }
    user: User = User.query.filter_by(email=data['email']).first()
    if not user:
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if password1 == password2:
            data["password"] = password1
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            flash('User registered successfully!', category='success')
            login_user(user, remember=True)
        else:
            flash('Passwords do not match!', category='error')
    else:
        flash('Email already exists!', category='warning')
    return redirect(request.referrer)


@auth.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form.get('email'),
    }
    user: User = User.query.filter_by(email=data['email']).first()
    if user:
        password = request.form.get('password')
        if user.has_valid(password):
            login_user(user, remember=True)
            flash('User logged in successfully!', category='success')
        else:
            flash('Incorrect password!', category='error')
    else:
        flash('Email is not registered!', category='warning')
    return redirect(request.referrer)


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(request.referrer)
