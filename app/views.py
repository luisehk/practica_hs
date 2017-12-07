# -*- coding: utf-8 -*-
from app import app, db
from flask import render_template, redirect
from app.forms import CommentForm
from app.models import Comment


@app.route('/')
@app.route('/hola')
def hola():
    persons = [
        {
            'name': 'Jesus Lerma',
            'is_welcome': True
        },
        {
            'name': 'Luis Herrada',
            'is_welcome': False
        },
        {
            'name': 'Nomas Jorge',
            'is_welcome': True
        }
    ]

    return render_template(
        'index.html',
        persons=persons
    )


@app.route('/comentarios', methods=["GET", "POST"])
def comentarios():
    form = CommentForm()

    if form.validate_on_submit():
        c = Comment(
            author=form.author.data,
            text=form.text.data
        )

        db.session.add(c)
        db.session.commit()

        return redirect('/comentarios')

    return render_template(
        'comments.html',
        comments=Comment.query.all(),
        form=form
    )
