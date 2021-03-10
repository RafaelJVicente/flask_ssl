import os
import subprocess
import sys
import unittest
from multiprocessing import Process

import requests
from requests import Response

from app import *


def start_app():
    serving.run_simple(API_HOST, API_PORT, app, ssl_context=context)


class TestFlaskSSL(unittest.TestCase):
    def setUp(self):
        self.server = Process(target=start_app)
        self.server.start()

    def tearDown(self):
        self.server.terminate()
        self.server.join()

    def test_request(self):
        response: Response = requests.get(f'https://{API_HOST}:{API_PORT}', cert=(API_CRT, API_KEY), verify=API_CA_CRT)
        self.assertEqual(response.text, API_TEXT)

    def test_curl_pem(self):
        proc = subprocess.Popen(
            ["curl", "--cacert", API_CA_CRT, "-E", f"{API_CRT.stem}.pem", f"https://{API_HOST}:{API_PORT}/"]
            , stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        (response, err) = proc.communicate()
        self.assertEqual(response.decode(), API_TEXT)

    def test_curl_crt_key(self):
        proc = subprocess.Popen(
            ["curl", "--cacert", API_CA_CRT, "--cert", API_CRT, "--key", API_KEY, f"https://{API_HOST}:{API_PORT}/"]
            , stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        (response, err) = proc.communicate()
        self.assertEqual(response.decode(), API_TEXT)


if __name__ == '__main__':
    unittest.main()
