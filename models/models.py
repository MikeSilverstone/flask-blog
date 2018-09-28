from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from globals.globals import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',
                            backref='author',
                            lazy='dynamic',
                            primaryjoin="User.id == Post.user_id")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def get_user(self, username):
        res = self.query.filter_by(username=username).first()
        return res

    def get_posts_by_user(self, id):
        res = self.query.filter_by(id=id).first()
        if res:
            return res.posts
        return None


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    body = db.Column(db.String(1000), index=True, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr(self):
        return 'Post {}'.format(self.body)

    def add_post(self):
        db.session.add(self)
        db.session.commit()

    def get_post(self, id):
        res = self.query.filter_by(id=id).first()
        return res
