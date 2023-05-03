"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcZsL6PVn0SNiabAKz7js0QknS2ilJam19QQ&usqp=CAU'
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.Text, nullable = False)
    lastname = db.Column(db.Text, nullable = False)
    imageurl = db.Column(db.Text, nullable = False, default = img_url)
    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
def connect_db(app):
    db.app = app
    db.init_app(app)