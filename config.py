import os


basedir = os.path.abspath(
    os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(
    basedir, 'db_repository')


WTF_CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'


TWILIO_API_KEY = 'AC692d2817750e01a0b7face1accd0030f'
TWILIO_TEST_AUTHTOKEN = 'bbece6bd20ac6663b4c0eacad21d43b6'
TWILIO_PHONE_NUMBER = '+525541637118'
