import os


class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///db/shorten_url.db"
    SERVER_PORT = os.environ.get("TORNADO_PORT") or 8888
    PROJECT_BASE = os.path.abspath(os.path.dirname(__file__))
    TEMPLATES_DIR = f"{PROJECT_BASE}/templates"
