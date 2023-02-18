from http.server import HTTPServer

from settings import PORT
from views.api import ApiViews

if __name__ == "__main__":
    httpd = HTTPServer(('', PORT), ApiViews)
    print(f'Starting server {PORT}')
    httpd.serve_forever()
