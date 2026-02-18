#!/usr/bin/env python3
"""
This module implements a simple HTTP server that provides basic API
endpoints returning plain text or JSON responses.
"""

import http.server
import json


class Handler(http.server.SimpleHTTPRequestHandler):
    """
    This class handles HTTP GET requests for different API endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests and returns responses based on the request path.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_data = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.end_headers()
            self.wfile.write(json_data)

        else:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 not found")


server = http.server.HTTPServer(("localhost", 8000), Handler)

print("Serveur lancé sur http://localhost:8000")
server.serve_forever()
