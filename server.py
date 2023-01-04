import os
import http.server

# change the working directory to the directory this file is located in
os.chdir(os.path.dirname(os.path.abspath(__file__)))


HandlerClass = http.server.SimpleHTTPRequestHandler

# Patch in the correct extensions
HandlerClass.extensions_map['.js'] = 'application/javascript'

# Run the server (like `python -m http.server` does)
http.server.test(HandlerClass, port=8000)
