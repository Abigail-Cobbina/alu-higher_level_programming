#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/route_5")
def route():
    if request.headers.get("X-HolbertonSchool-User-Id") == "98":
        return "Hello Holberton School!"
    return "NOP"

app.run(host="0.0.0.0", port=5000)
