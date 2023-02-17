from http.server import HTTPServer

from settings import HOST, PORT
from views.api import ApiViews

if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), ApiViews)
    print(f'Starting server {HOST} {PORT}')
    httpd.serve_forever()
