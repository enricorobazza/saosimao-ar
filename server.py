from http.server import SimpleHTTPRequestHandler
import ssl
from socketserver import TCPServer

httpd = TCPServer(('0.0.0.0', 8001), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="./.cert/key.pem", 
        certfile='./.cert/cert.pem', server_side=True)

httpd.serve_forever()