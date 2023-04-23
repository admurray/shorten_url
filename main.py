import asyncio

from sqlalchemy import create_engine
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado_sqlalchemy import SQLAlchemy

from config import Config
from handlers import ShortenURLHandler, IndexHandler, RedirectHandler


def make_app():
    return Application([
        (r"/", IndexHandler),
        (r"/s/(\w+)", RedirectHandler),
        (r"/shorten", ShortenURLHandler),
    ], db=SQLAlchemy(Config.DATABASE_URL))


async def main():
    app = make_app()
    app.listen(Config.SERVER_PORT)
    await asyncio.Event().wait()


if __name__ == "__main__":
    io_loop = IOLoop.current()

    # create Tornado application
    app = make_app()

    # start listening
    app.listen(Config.SERVER_PORT)
    io_loop.start()
