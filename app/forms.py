from flask_wtf import Form
from wtforms import StringField, TextAreaField, validators


class CommentForm(Form):
    author = StringField(
        'Autor',
        validators=[
            validators.DataRequired()
        ]
    )
    text = TextAreaField(
        'Comentario',
        validators=[
            validators.DataRequired()
        ]
    )
