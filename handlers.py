from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin

from model import URLMapping
from schema import URLMappingSchema
from utilities import get_short_url_id, get_short_url


class IndexHandler(SessionMixin, RequestHandler):
    def get(self):
        self.render('templates/index.html')


class ShortenURLHandler(SessionMixin, RequestHandler):
    def get(self):
        self.render('templates/index.html')

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
            url_mapping_schema = URLMappingSchema()
            serialized_mapping = url_mapping_schema.dump(url_mapping)

        self.render(
            "templates/shorten.html",
            short_url=get_short_url(short_url_id),
            base_url=f"{self.request.protocol}://{self.request.host}"
        )


class RedirectHandler(SessionMixin, RequestHandler):
    def get(self, short_url_id):
        with self.make_session() as session:
            url_mapping = session.query(URLMapping).filter(
                URLMapping.short_url_id == short_url_id).first()
            long_url = url_mapping.long_url
        self.redirect(long_url)
