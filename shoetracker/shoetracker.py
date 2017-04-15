"""
    ShoeTracker
    
    A simple API for tracking the miles on your shoes.
    
    :copyright: (c) 2017 by Nicholas Lawrence
    :license: BSD, see LICENSE.txt for details
"""
import os
from flask import Flask, jsonify, request, abort
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


@app.route('/shoes', methods=['POST'])
def add_shoe():
    if request.is_json:
        data = request.get_json()

        # Validate we actually have a name to work with
        if not data or 'name' not in data:
            abort(400)

        name = data['name'] #TODO: Test for SQLi

        shoe = Shoe(name=name)
        db.session.add(shoe)
        db.session.commit()

        return jsonify({'id': shoe.id, 'name': shoe.name})
    else:
        abort(415)
