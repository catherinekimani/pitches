from . import db

class User(db.Model):
    pass

class Pitch(db.Model):
    pass

class Comments(db.Model):
    pass 

class Upvotes(db.Model):
    pass

class Downvotes(db.Model):
    pass


    def __repr__(self):
        return f'User {self.username}'