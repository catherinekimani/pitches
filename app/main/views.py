from crypt import methods
from unicodedata import category
from flask import render_template,request,redirect,url_for,abort
from .. models import User,Pitch,Upvotes,Downvotes,Comments
from . import main
from . forms import UpdateProfile
from .. import db,photos
from flask_login import login_required

@main.route('/')
def index():
    pitches = Pitch.query.all()
    print(pitches)
    tech = Pitch.query.filter_by(category = 'Tech').all()
    inspirational = Pitch.query.filter_by(category= 'Inspirational').all()
    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html',pitches=pitches,tech = tech,inspirational=inspirational)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html',user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile',uname = user.username))
    return render_template('/profile/update.html',form = form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))