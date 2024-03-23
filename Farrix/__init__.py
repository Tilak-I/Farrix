import http.server
import socketserver

web_title = ""

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def generate_html_content(self):
        # Generate HTML content with the dynamic title
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{web_title}</title>
        </head>
        <body>
            <h1></h1>
        </body>
        </html>
        """
        return html_content

    def do_GET(self):
        global web_title
        # Send the HTTP response header
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Generate the HTML content with the updated title
        html_content = self.generate_html_content()
        
        # Write the HTML content to the response
        self.wfile.write(html_content.encode('utf-8'))

def start_server(title : str, port=8000):
    global web_title
    web_title = title
    # Set up the HTTP server
    Handler = CustomRequestHandler

    # Create a socket server
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Server started at port", port)
        print("http://localhost:8000/")
        httpd.serve_forever()
