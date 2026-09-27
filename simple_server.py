# simple_server.py
import http.server
import socketserver
import json
import time

PORT = 8888

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Get the length of the incoming data
        content_length = int(self.headers['Content-Length'])
        # Read the data
        post_data = self.rfile.read(content_length)

        # Decode and print the received data for debugging
        received_json = json.loads(post_data.decode('utf-8'))
        print(f"Received Question: {received_json.get('question')}")

        # --- Prepare the response ---
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Create the response payload
        response_payload = {
            "answer": f"The python server received your question: '{received_json.get('question')}'",
            "status": "success_from_python"
        }

        # Write the response back to the client
        self.wfile.write(bytes(json.dumps(response_payload), "utf8"))
        return

# This sets up and runs the server
Handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Python server running at port", PORT)
    httpd.serve_forever()