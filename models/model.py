from sqlalchemy import Column, String, Integer
from tornado_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy(url=Config.DATABASE_URL)


class URLMapping(db.Model):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    long_url = Column(String(255), unique=False)
    short_url_id = Column(String(255), unique=True)
