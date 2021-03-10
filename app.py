from pathlib import Path

from flask import Flask
from werkzeug import serving

import ssl

HTTPS_ENABLED = True
VERIFY_CLIENT = True

API_HOST = "localhost"
API_PORT = 8000

# API_CRT = "server.crt"
# API_KEY = "server.key"
API_CRT = Path("client.crt")
API_KEY = Path("client.key")
API_CA_CRT = Path("root_ca.crt")
API_TEXT = "Hello api"

assert API_CRT.is_file(), f'Invalid path: {API_CRT.absolute()}'
assert API_KEY.is_file(), f'Invalid path: {API_KEY.absolute()}'
assert API_CA_CRT.is_file(), f'Invalid path: {API_CA_CRT.absolute()}'


app = Flask(__name__)


@app.route("/")
def main():
    return API_TEXT


context = None
if HTTPS_ENABLED:
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    if VERIFY_CLIENT:
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(API_CA_CRT)
        context.load_cert_chain(API_CRT, API_KEY)


if __name__ == '__main__':
    serving.run_simple(API_HOST, API_PORT, app, ssl_context=context)
