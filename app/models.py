from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import  login_manager
from datetime import datetime
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic = db.Column(db.String())
    
    # create relationship
    pitches = db.relationship('Pitch',backref = 'pitch',lazy = 'dynamic')
    comments = db.relationship('Comments',backref = 'pitch', lazy = 'dynamic')
    upvotes = db.relationship('Upvotes', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relationship('Downvotes', backref = 'pitch', lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the passwrd attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(30),nullable=False)
    description = db.Column(db.Text, nullable=False )
    user = db.Column(db.String, nullable=False)
    category = db.Column(db.String(150), index = True,nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    
    def __repr__(self):
        return f'User {self.category}'
    
class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f'User {self.text}'
    
class Upvotes(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f'User {self.user_id}'
    
class Downvotes(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.user_id}'
    
    # python3 manage.py db migrate -m "Change password name Migration"
    # python3 manage.py db upgrade