from flask import Flask, render_template, send_from_directory, request, Response
import os
import asyncio
from threading import Thread
import requests
from io import BytesIO
from PIL import Image
app = Flask('Calculator')

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "base-uri 'self'"
    return response

@app.route('/')
def main():
    return render_template("index.html")

def run():
    app.run(host="0.0.0.0", port=9492)    

def serveron():
    site = Thread(target=run)
    site.start()

