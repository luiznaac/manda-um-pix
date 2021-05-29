from http.server import BaseHTTPRequestHandler, HTTPServer
from request_handler import RequestHandler
from socketserver import ThreadingMixIn
import web

request_handler: RequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        request_handler.handle(self)

    def log_message(self, format, *args):
        pass


class ThreadingHandler(ThreadingMixIn, HTTPServer):
    pass


def run():
    create_context()
    server_address = ('', 80)
    server = ThreadingHandler(server_address, Handler)
    server.serve_forever()


def create_context():
    global request_handler
    request_handler = RequestHandler()

    request_handler.link_handler('/', web.index)
    request_handler.link_handler('/images/lansa_um_pix.jpeg', web.braba_image)


if __name__ == '__main__':
    run()
