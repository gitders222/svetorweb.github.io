# config.py

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Replace with your database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
