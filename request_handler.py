from http.server import BaseHTTPRequestHandler


class RequestHandler:

    handlers_link = {}

    def link_handler(self, endpoint, handler):
        self.handlers_link.update({endpoint: handler})

    def handle(self, request: BaseHTTPRequestHandler):
        handler = self.handlers_link[request.path]

        response = handler()

        request.send_response(200)
        request.send_header('Content-type', response['content_type'])
        request.end_headers()
        request.wfile.write(response['contents'])
