from shoetracker.shoetracker import db


class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Shoe %r>' % self.id
