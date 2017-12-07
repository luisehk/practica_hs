from app import db


class Comment(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True)
    author = db.Column(
        db.String(30),
        index=False,
        unique=False)
    text = db.Column(
        db.Text,
        index=False,
        unique=False)
