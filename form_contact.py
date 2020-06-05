from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Name should be filled')])
    email = StringField('E-mail', validators=[DataRequired('E-mail should be filled'),Email('Invalid email id')])
    subject = StringField('Subject', validators=[DataRequired('Subject must be filled')])
    message = TextAreaField('Message', validators=[DataRequired('Message must be filled')])
    submit = SubmitField("Send")