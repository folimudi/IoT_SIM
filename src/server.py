import requests
import random
import time
import json
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, jsonify
from main import *

app = Flask(__name__)

url = "https://c01-usa-east-et.integrate-test.boomi.com/ws/simple/createReading;boomi_auth=bGFtYmRhQGJvb21pX2p1YW5yb2RyaWd1ZXotNEEwWlpDLlZKUTlSUjoyN2UzZjQzNS1lZWY1LTQ0ZGItOTExOS1jZGIwMDBjNzIzMjA="

def handler():
    main()
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Status ": "Executed simulation completely"
        })
    }

@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    response = handler()
    return jsonify(response["body"]), response["statusCode"], response["headers"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)