from flask import Blueprint, request, redirect, flash
from flask_login import login_required, current_user

from website.utils import titlecase
from .models import Word, Meaning, Example
from . import db

forms = Blueprint('forms', __name__)


@forms.route('/add-word', methods=['POST'])
@login_required
def add_word():
    # print(request.form)  # TEST LINE
    data = {
        'word': request.form['word'],
        'pos': request.form['pos'],
    }
    word = Word.query.filter_by(word=data['word'], pos=data['pos']).first()
    if not word:
        word = Word(**data)
        # print(word)  # TEST LINE
        db.session.add(word)
        db.session.commit()
        flash('Word added successfully!', 'success')
    else:
        flash('Word already exists!', 'warning')
    return redirect(request.referrer)


@forms.route('/add-meaning', methods=['POST'])
@login_required
def add_meaning():
    # print(request.form)  # TEST LINE
    data = {
        'meaning': request.form['meaning'],
        'source': titlecase(request.form['source']),
        'word_id': request.form['word_id'],
    }
    meaning = Meaning.query.filter_by(meaning=data['meaning'], source=data['source'], word_id=data['word_id']).first()
    if not meaning:
        meaning = Meaning(**data)
        # print(meaning)  # TEST LINE
        db.session.add(meaning)
        db.session.commit()
        flash('Meaning added successfully!', )
    else:
        flash('Meaning already exists!', 'warning')
    return redirect(request.referrer)


@forms.route('/add-example', methods=['POST'])
@login_required
def add_example():
    # print(request.form)  # TEST LINE
    data = {
        'example': request.form['example'],
        'word_id': request.form['word_id'],
        'user': current_user,
    }
    example = Example.query.filter_by(example=data['example'], word_id=data['word_id']).first()
    if not example:
        example = Example(**data)
        # print(example)  # TEST LINE
        db.session.add(example)
        db.session.commit()
        flash('Example added successfully!', )
    else:
        flash('Example already exists!', 'warning')
    return redirect(request.referrer)
