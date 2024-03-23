# __init__.py

import http.server
import socketserver

def start_server(port=8000):    #Start a simple HTTP server serving a blank page
    class EmptyPageHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # Send the HTTP response header
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Send the HTML content (empty in this case)
            self.wfile.write(b"<html><head><title>Blank Page</title></head><body></body></html>")

    # Set up the HTTP server
    Handler = CustomRequestHandler

    # Create a socket server
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Server started at port", port)
        print("http://localhost:8000/")
        httpd.serve_forever()


class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Initialize HTML content variable
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dynamic Server</title>
    </head>
    <body>
        <h1>Welcome to the Dynamic Server!</h1>
    </body>
    </html>
    """

    def do_GET(self):
        # Send the HTTP response header
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Write the HTML content to the response
        self.wfile.write(self.html_content.encode('utf-8'))

def add_element():
    # Update the HTML content variable by adding a new element
    CustomRequestHandler.html_content += "<p>New element added!</p>"

