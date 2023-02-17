import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from algorithms.sort import get_sorted_list
from algorithms.vowel_count import get_vowel_count
from models.sort import InputSortModel
from models.vowel_count import InputVowelCountModel


class ApiViews(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            payload = self.get_payload()
            if self.is_valid_content_type():
                if self.path == '/vowel_count':
                    input_vowel_count_model_payload = InputVowelCountModel(**payload)
                    response, status_code = self.create_response_vowel_count(input_vowel_count_model_payload)
                elif self.path == '/sort':
                    input_sort_model_payload = InputSortModel(**payload)
                    response, status_code = self.create_response_sort(input_sort_model_payload)
                else:
                    response, status_code = {'error_message': f'non-existent route {self.path}'}, HTTPStatus.NOT_FOUND
            else:
                response, status_code = {'error_message': 'Content-Type is not application/json'}, \
                    HTTPStatus.UNSUPPORTED_MEDIA_TYPE
        except ValueError as error:
            response, status_code = {'error_message': str(error)}, HTTPStatus.BAD_REQUEST

        self.build_response(response, status_code)

    def is_valid_content_type(self) -> bool:
        content_type = self.headers['Content-Type']
        if content_type != 'application/json':
            return False
        return True

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

    def build_response(self, response: dict, status_code: HTTPStatus) -> None:
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode(encoding='utf_8'))
