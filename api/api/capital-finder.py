from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        
        self.send_response(200)  #200 means ok
        self.send_header('Content-type','text/plain')
        self.end_headers()