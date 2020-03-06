import os
import multiprocessing

# flask settings
FLASK_HOST = os.environ.get('FLASK_ROUTE', '0.0.0.0')
FLASK_PORT = os.environ.get('FLASK_PORT', '5000')
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', True)

# gunicorn settings
bind = os.environ.get('GUNICORN_BIND', f'{FLASK_HOST}:{FLASK_PORT}')
workers = os.environ.get('GUNICORN_WORKERS', 1)  # multiprocessing.cpu_count() * 2 + 1
reload = FLASK_DEBUG

# sql alchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
