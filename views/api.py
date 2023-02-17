import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from algorithms.sort import get_sorted_list
from algorithms.vowel_count import get_vowel_count
from models.sort import InputSortModel
from models.vowel_count import InputVowelCountModel


class ApiViews(BaseHTTPRequestHandler):

    def do_POST(self):
        payload = self.get_payload()

        try:
            if self.path == '/vowel_count':
                input_vowel_count_model_payload = InputVowelCountModel(**payload)
                response, status_code = self.create_response_vowel_count(input_vowel_count_model_payload)

            if self.path == '/sort':
                input_sort_model_payload = InputSortModel(**payload)
                response, status_code = self.create_response_sort(input_sort_model_payload)

        except ValueError as error:
            response, status_code = {'error_message': str(error)}, HTTPStatus.BAD_REQUEST

        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode(encoding='utf_8'))

    def get_payload(self) -> json:
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body)

    @staticmethod
    def create_response_vowel_count(payload: InputVowelCountModel) -> tuple[dict, HTTPStatus]:
        response = {}
        for word in payload.words:
            response[word] = get_vowel_count(word)
        status_code = HTTPStatus.OK

        return response, status_code

    @staticmethod
    def create_response_sort(payload: InputSortModel) -> tuple[list, HTTPStatus]:
        map_order_reverse_list = {
            'asc': False,
            'desc': True
        }

        sorted_list = get_sorted_list(payload.words, reverse=map_order_reverse_list[payload.order])
        status_code = HTTPStatus.OK

        return sorted_list, status_code
