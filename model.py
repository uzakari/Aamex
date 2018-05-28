from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_moment import Moment
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/ads'
admin = Admin(app)
app.secret_key = 'itissupposetobesecret'
boo = Bootstrap(app)
db = SQLAlchemy(app)
moment = Moment(app)
manger = Manager(app)
migrate = Migrate(app, db)

manger.add_command('db', MigrateCommand)

login_manger = LoginManager(app)
login_manger.login_view = 'login'


class Signup(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    items = db.relationship('Additemmodel', backref='Signup', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.name


@login_manger.user_loader
def load_user(user_id):
    return Signup.query.get(int(user_id))


class Additemmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    sender_name = db.Column(db.String(30))
    sender_number = db.Column(db.String(30))
    recipient_name = db.Column(db.String(30))
    recipient_number = db.Column(db.String(20))
    delivery_mode = db.Column(db.String(25))
    services = db.Column(db.String(15))
    payment = db.Column(db.String(20))
    address = db.Column(db.String(400))
    Item_Deliver = db.Column(db.String(500))
    signUp_id = db.Column(db.Integer, db.ForeignKey('signup.id'))

    def __repr__(self):
        return '<Product  %r>' % self.sender_number



if __name__ == '__main__':
    manger.run()
    # app.run(port=3212)