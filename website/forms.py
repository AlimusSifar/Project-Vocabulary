from flask import Blueprint, request, redirect, flash
from flask_login import login_required, current_user

from website.utils import titlecase
from .models import Word, Meaning, Example
from . import db

forms = Blueprint('forms', __name__)


@forms.route('/add-word', methods=['POST'])
@login_required
def add_word():
    data = {
        'word': request.form['word'],
        'pos': request.form['pos'],
        'user': current_user,
    }
    word = Word.query.filter_by(word=data['word'], pos=data['pos']).first()
    if not word:
        word = Word(**data)
        db.session.add(word)
        db.session.commit()
        flash('Word added successfully!', category='success')
    else:
        flash('Word already exists!', category='warning')
    return redirect(request.referrer)


@forms.route('/add-meaning', methods=['POST'])
@login_required
def add_meaning():
    data = {
        'meaning': request.form['meaning'],
        'source': titlecase(request.form['source']),
        'word_id': request.form['word_id'],
        'user': current_user,
    }
    meaning = Meaning.query.filter_by(meaning=data['meaning'], source=data['source'], word_id=data['word_id']).first()
    if not meaning:
        meaning = Meaning(**data)
        db.session.add(meaning)
        db.session.commit()
        flash('Meaning added successfully!', category='success', )
    else:
        flash('Meaning already exists!', category='warning')
    return redirect(request.referrer)


@forms.route('/add-example', methods=['POST'])
@login_required
def add_example():
    data = {
        'example': request.form['example'],
        'word_id': request.form['word_id'],
        'user': current_user,
    }
    example = Example.query.filter_by(example=data['example'], word_id=data['word_id']).first()
    if not example:
        example = Example(**data)
        db.session.add(example)
        db.session.commit()
        flash('Example added successfully!', category='success', )
    else:
        flash('Example already exists!', category='warning')
    return redirect(request.referrer)
