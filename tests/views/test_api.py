import subprocess
import sys
import time
from http import HTTPStatus

import pytest
import requests
from settings import PORT

URL_BASE = f'http://localhost:{PORT}'


@pytest.fixture(autouse=True, scope="session")
def start_server():
    executable_app = f'{sys.path[0]}/main.py'
    ds_proc = subprocess.Popen(
        [
            sys.executable,
            executable_app
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    time.sleep(2)
    assert not ds_proc.poll(), ds_proc.stdout.read().decode("utf-8")
    yield ds_proc
    ds_proc.terminate()


def test_vowel_count_ok():
    url = f'{URL_BASE}/vowel_count'
    response = requests.post(url, json={'words': ['batman', 'robin', 'coringa']})
    assert response.status_code == HTTPStatus.OK
    assert response.text == '{"batman": 2, "robin": 2, "coringa": 3}'


def test_vowel_count_fail_without_field_required_payload():
    url = f'{URL_BASE}/vowel_count'
    response = requests.post(url, json={'w': ['batman', 'robin', 'coringa']})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.text == '{"error_message": "1 validation error for InputVowelCountModel\\' \
                            'nwords\\n  field required (type=value_error.missing)"}'


def test_vowel_count_fail_without_list_in_words_payload():
    url = f'{URL_BASE}/vowel_count'
    response = requests.post(url, json={'words': 1})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.text == '{"error_message": "1 validation error for InputVowelCountModel\\' \
                            'nwords\\n  value is not a valid list (type=type_error.list)"}'


def test_sort_asc_ok():
    url = f'{URL_BASE}/sort'
    response = requests.post(url, json={'words': ['batman', 'robin', 'coringa'], 'order': 'asc'})
    assert response.status_code == HTTPStatus.OK
    assert response.text == '["batman", "coringa", "robin"]'


def test_sort_desc_ok():
    url = f'{URL_BASE}/sort'
    response = requests.post(url, json={'words': ['batman', 'robin', 'coringa'], 'order': 'desc'})
    assert response.status_code == HTTPStatus.OK
    assert response.text == '["robin", "coringa", "batman"]'


def test_sort_fail_without_fields_required_payload():
    url = f'{URL_BASE}/sort'
    response = requests.post(url, json={'w': ['batman', 'robin', 'coringa'], 'o': 'asc'})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.text == '{"error_message": "2 validation errors for InputSortModel\\nwords\\' \
                            'n  field required (type=value_error.missing)\\norder\\' \
                            'n  field required (type=value_error.missing)"}'


def test_sort_fail_invalid_values_payload():
    import json

    url = f'{URL_BASE}/sort'
    response = requests.post(url, json={'words': 1, 'order': 'nenhuma'})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert json.loads(response.content) == {
        'error_message': "2 validation errors for InputSortModel\nwords\n  value is not a valid list "
                         "(type=type_error.list)\norder\n  unexpected value; permitted: 'asc', 'desc' "
                         "(type=value_error.const; given=nenhuma; permitted=('asc', 'desc'))"}


def test_fail_non_existent_route():
    url = f'{URL_BASE}/test'
    response = requests.post(url, json={})
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.text == '{"error_message": "non-existent route /test"}'


def test_fail_invalid_content_type():
    url = f'{URL_BASE}/sort'
    response = requests.post(url, json={}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    assert response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    assert response.text == '{"error_message": "Content-Type is not application/json"}'
