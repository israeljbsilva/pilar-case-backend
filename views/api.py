import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from algorithms.vowel_count import get_vowel_count
from algorithms.sort import get_sorted_list


class ApiViews(BaseHTTPRequestHandler):

    def do_POST(self):
        payload = self.get_payload()

        if self.path == '/vowel_count':
            response, status_code = self.create_response_vowel_count(payload)

        if self.path == '/sort':
            response, status_code = self.create_response_sort(payload)

        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode(encoding='utf_8'))

    def get_payload(self) -> json:
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body)

    @staticmethod
    def create_response_vowel_count(payload: json) -> tuple[dict, HTTPStatus]:
        response = {}
        for word in payload.get('words'):
            response[word] = get_vowel_count(word)
        status_code = HTTPStatus.OK

        return response, status_code

    @staticmethod
    def create_response_sort(payload: json) -> tuple[list, HTTPStatus]:
        map_order_reverse_list = {
            'asc': False,
            'desc': True
        }

        words = payload.get('words')
        order = payload.get('order')

        sorted_list = get_sorted_list(words, reverse=map_order_reverse_list[order])
        status_code = HTTPStatus.OK

        return sorted_list, status_code
