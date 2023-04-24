import sys
import os

from sqlalchemy import Column, String, Integer, Table, MetaData, create_engine, inspect

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.url_mapping import URLMapping
from config import Config


def _create_table_if_not_exists(tablename):
    engine = create_engine(Config.DATABASE_URL)

    if not inspect(engine).has_table(URLMapping.__tablename__):
        metadata = MetaData(engine)
        # Create a table with the appropriate Columns
        Table(tablename, metadata,
              Column('ID', Integer, primary_key=True),
              Column('LONG_URL', String(255), unique=False),
              Column('SHORT_URL_ID', String(255), unique=True), )
        # Implement the creation
        metadata.create_all()


if __name__ == "__main__":
    _create_table_if_not_exists(URLMapping.__tablename__)
