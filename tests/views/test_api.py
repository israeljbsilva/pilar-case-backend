import subprocess
import sys
import time
from http import HTTPStatus

import pytest
import requests

from settings import HOST, PORT


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
    url = f'http://{HOST}:{PORT}/vowel_count'
    response = requests.post(url, json={'words': ['batman', 'robin', 'coringa']})
    assert response.status_code == HTTPStatus.OK
    assert response.text == '{"batman": 2, "robin": 2, "coringa": 3}'


def test_sort_asc_ok():
    url = f'http://{HOST}:{PORT}/sort'
    response = requests.post(url, json={'words': ['batman', 'robin', 'coringa'], 'order': 'asc'})
    assert response.status_code == HTTPStatus.OK
    assert response.text == '["batman", "coringa", "robin"]'


def test_sort_desc_ok():
    url = f'http://{HOST}:{PORT}/sort'
    response = requests.post(url, json={'words': ['batman', 'robin', 'coringa'], 'order': 'desc'})
    assert response.status_code == HTTPStatus.OK
    assert response.text == '["robin", "coringa", "batman"]'
