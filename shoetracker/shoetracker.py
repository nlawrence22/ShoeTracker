"""
    ShoeTracker
    
    A simple API for tracking the miles on your shoes.
    
    :copyright: (c) 2017 by Nicholas Lawrence
    :license: BSD, see LICENSE.txt for details
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)

# We need to import our models so they can be created by create
# scripts, but this has to come after the definition of db to avoid
# circular import issues.
from shoetracker.models import Shoe


@app.route('/')
def hello_world():
    return 'Hello, World!'
