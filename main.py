import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
from flask import render_template, flash, redirect, request
from forms.forms import LoginForm
from models.models import User, Post
from globals.globals import app
from flask_login import current_user, login_user, logout_user


@app.route("/")
def index():
    return render_template('base.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if current_user.is_authenticated:
            flash('You are already logged in')
            return redirect('/login')

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')

        login_user(user, remember=form.remember_me.data)

        return redirect('/')

    return render_template('login.html', title='Sign In', form=form)


@app.route("/logout", methods=['GET', "POST"])
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have successfully logged out.')
        return redirect('/')

    flash('You are not logged in.')
    return redirect('/')


@app.route("/register", methods=['GET', 'POST'])  # TODO
def register():
    form = LoginForm()
    return None


@app.route("/user/<string:username>", methods=['GET', 'POST'])
def user(username):
    u = User()
    user = u.get_user(username=username)

    title = request.form.get('new-title')
    body = request.form.get('new-body')

    if title and body:
        p = Post(title=title, body=body, user_id=user.id)
        p.add_post()

    posts = u.get_posts_by_user(user.id)

    if not posts:
        posts = [
            Post(id=2, title="There's nothing here yet!", body="There's nothing here yet!", user_id=-1)
        ]

    if user:
        return render_template('user_page.html', username=user.username, posts=posts)

    return "user not found"  # TODO change the custom 404
