# from crypt import methods
# from msilib import CAB
# from unicodedata import category
from flask import render_template,request,redirect,url_for,abort
from .. models import User,Pitch,Upvotes,Downvotes,Comments
from . import main
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
from flask_login import current_user, login_required

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

# new pitch
@main.route('/new_pitch', methods=['GET','POST'])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        category = form.category.data
        user_id  = current_user
        new_pitch_object = Pitch(description=description,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html',form = form)

# comments
@main.route('/comments/<int:pitch_id>', methods=['GET','POST'])
@login_required
def new_comments(pitch_id):
    comments = Comments.get_comments(pitch_id)
    pitches = Pitch.query.get(pitch_id)
    pitch_by = Pitch.user_id
    user = User.query.filter_by(id=pitch_by).first()
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data      
        new_comment = Comments(text=comment, pitch_id=pitch_id, user_id=current_user.get_id())
        new_comment.save_comment()
        # return redirect(url_for('main.index',pitch_id = pitch_id))

    return render_template('comments.html',Commentsform=form, comments=comments, pitches = pitches, user=user)

# likes
@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_pitches = Upvotes.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitches in get_pitches:
        to_str = f'{pitches}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_like = Upvotes(pitch_id=id)
    new_like.save()
    return redirect(url_for('main.index',id=id))

# dislikes

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    get_pitches = Downvotes.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitches in get_pitches:
        to_str = f'{pitches}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_dislike = Downvotes(pitch_id=id)
    new_dislike.save()
    return redirect(url_for('main.index',id=id))

# profile

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html',user = user,pitches=pitches)

# update profile

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
        # print(current_user)
        return redirect(url_for('.profile',uname = user.username))
    return render_template('/profile/update.html',form = form)

# update pic

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