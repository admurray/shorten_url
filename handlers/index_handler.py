from tornado_sqlalchemy import SessionMixin
from tornado.web import RequestHandler

from config import Config


class IndexHandler(SessionMixin, RequestHandler):
    async def get(self):
        await self.render(f'{Config.TEMPLATES_DIR}/index.html')
