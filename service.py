import os
from flask import Flask, jsonify, json

app = Flask(__name__)

# GET /
@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    print "Hello World Service Starting..."
    debug = (os.getenv('DEBUG', 'False') == 'True')
    port = os.getenv('PORT', '5000')
    app.run(host='0.0.0.0', port=int(port), debug=debug)
