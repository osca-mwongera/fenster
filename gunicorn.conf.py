"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import getenv

from dotenv import load_dotenv

load_dotenv()


def max_workers():
    return cpu_count()


port: int = getenv('PORT', 8000)
bind = f'0.0.0.0:{port}'
wsgi_app: str = "fenster.wsgi"
reload: bool = True
reload_extra_files: list = []
workers: int = max_workers() * 2 + 1
