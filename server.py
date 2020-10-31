import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)

        
        self.send_header("Content-type", "text/html")

        
        self.end_headers()

  
        name = 'Stranger'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components["name"][0]

       
        html = f"<html><head></head><body><h1>Hello {name}!</h1></body></html>"

       
        self.wfile.write(bytes(html, "utf8"))

        return


handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)


my_server.serve_forever()