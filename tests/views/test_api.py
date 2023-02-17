import subprocess
import sys
import time

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
    response = requests.post(url, json={'vowel_count': 'test'})
    assert response.status_code == 200
    assert response.text == '{"vowel_count": "test"}'


def test_sort_ok():
    url = f'http://{HOST}:{PORT}/sort'
    response = requests.post(url, json={'sort': 'test'})
    assert response.status_code == 200
    assert response.text == '{"sort": "test"}'
