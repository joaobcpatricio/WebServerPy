from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200) #200 means reached a page successefully
        except:
            file_to_open = "File not found"
            self.send_response(404) #404 means fail to reach the page
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))  #convert the text to be displayed from the file


httpd = HTTPServer(('localhost', 8080), Serv)   #httpd as it runs in the background
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    # Clean-up server (close socket, etc.)
    httpd.server_close()
