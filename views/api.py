import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler


class ApiViews(BaseHTTPRequestHandler):

    def do_POST(self):
        payload = self.get_payload()

        if self.path == '/vowel_count':
            response = json.dumps(payload).encode(encoding='utf_8')
            status_code = HTTPStatus.OK

        if self.path == '/sort':
            response = json.dumps(payload).encode(encoding='utf_8')
            status_code = HTTPStatus.OK

        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response)

    def get_payload(self) -> json:
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body)
