#!/usr/bin/env python3
"""
Simple HTTP server for Effective Mobile DevOps test assignment.
Responds with "Hello from Effective Mobile!" on GET / requests.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    """Handler for HTTP requests."""
    
    def do_GET(self):
        """Handle GET requests to the root path."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        """Log HTTP requests to stdout."""
        print(f"{self.address_string()} - [{self.log_date_time_string()}] {format % args}")


def run_server(port=8080):
    """Start the HTTP server on the specified port."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
