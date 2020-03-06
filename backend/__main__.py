from backend import app
from backend import settings

if __name__ == '__main__':
    app.run(settings.FLASK_HOST, settings.FLASK_PORT, settings.FLASK_DEBUG)
