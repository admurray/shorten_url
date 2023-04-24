from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin
from models.url_mapping import URLMapping


class RedirectHandler(SessionMixin, RequestHandler):
    async def get(self, short_url_id):
        with self.make_session() as session:
            url_mapping = session.query(URLMapping).filter(
                URLMapping.short_url_id == short_url_id).first()
            long_url = url_mapping.long_url
        self.redirect(long_url)
