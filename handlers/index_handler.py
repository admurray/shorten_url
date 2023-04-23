from tornado_sqlalchemy import SessionMixin
from tornado.web import RequestHandler

from config import Config


class IndexHandler(SessionMixin, RequestHandler):
    def get(self):
        self.render(f'{Config.TEMPLATES_DIR}/index.html')
