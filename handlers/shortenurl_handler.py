from tornado_sqlalchemy import SessionMixin
from tornado.web import RequestHandler

from models.model import URLMapping
from utilities.utilities import get_short_url_id, get_short_url
from config import Config


class ShortenURLHandler(SessionMixin, RequestHandler):
    def get(self):
        self.render(f'{Config.TEMPLATES_DIR}/index.html')

    def post(self):
        longurl = self.get_argument("long_url").strip()

        with self.make_session() as session:
            db_url_mapping = session.query(URLMapping).filter(
                URLMapping.long_url == longurl).first()
            if db_url_mapping:
                url_mapping = db_url_mapping
            else:
                url_mapping = URLMapping(
                    long_url=longurl,
                    short_url_id=get_short_url_id()
                )

            session.add(url_mapping)
            short_url_id = url_mapping.short_url_id

        self.render(
            f"{Config.TEMPLATES_DIR}/shorten.html",
            short_url=get_short_url(short_url_id),
            base_url=f"{self.request.protocol}://{self.request.host}"
        )
