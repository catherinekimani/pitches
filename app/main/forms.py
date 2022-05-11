from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    
class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Inspirational','Inspirational'),('Love','Love'),('Educational','Educational')],validators=[DataRequired()])
    text = TextAreaField('Share Your Pitch', validators=[DataRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')