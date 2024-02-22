from blogwithflask import db

class User(db.Models):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(70), nullable=False, unique=True)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    