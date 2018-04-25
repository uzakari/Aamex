from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from wtforms.fields.html5 import DateField


class Login_Form(Form):
    email = StringField(validators=[Email()])
    password = PasswordField(Length(min=5, max=20))
    remember = BooleanField('remember me')
    submit = SubmitField('Login')


class signUP_form(Form):
    name = StringField()
    email = StringField(validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password',message='Password must match')])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')


class add_item(Form):
    date = DateField(format='%Y-%m-%d')
    sender_name = StringField('Senders name ', validators=[DataRequired()])
    sender_number = StringField('Senders number', validators=[DataRequired()])
    Recipient_name = StringField('Recipients name', validators=[DataRequired()])
    Recipent_number = StringField('Recipient Number', validators=[DataRequired()])
    Payment = StringField('Payment', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    Product = StringField('Product To deliver', validators=[DataRequired()])
    Delivery_mode = SelectField('Delivery mode', choices=[('Office to door', 'Office to door'), ('Door to door', 'Door to Door '), ('Door to office', 'Door to office'),('Office to Office', 'Office to Office')])
    Service = SelectField('State', choices=[('Abuja', 'ABJ - KD'), ('Kaduna', 'KD - ABJ'), ('Kano', 'Kano'), ('Lagos', 'Lagos')])
    submit = SubmitField('Submit')