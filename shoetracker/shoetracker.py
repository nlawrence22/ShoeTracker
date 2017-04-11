"""
    ShoeTracker
    
    A simple API for tracking the miles on your shoes.
    
    :copyright: (c) 2017 by Nicholas Lawrence
    :license: BSD, see LICENSE.txt for details
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'