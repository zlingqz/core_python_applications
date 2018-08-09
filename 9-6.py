#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def go_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print('Welcome to the machine...', end='')
        print('Press ^C once or twice to quit.')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting dowm server')
        server.socket.close()


if __name__ == '__main__':
    main()
