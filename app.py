"""Blogly application."""

from flask import Flask, redirect, render_template, request
from models import db, connect_db, Users


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def root():
    return redirect('/users')

@app.route('/users')
def users_index():
    users = Users.query.order_by(Users.lastname, Users.firstname).all()
    return render_template('users/index.html', users = users)

@app.route('/users/new', methods=['GET'])
def new_user_form():
    return render_template('/users.html')

@app.route('/users/new', methods=['POST'])
def new_user():
    new_user_info = Users(
        firstname = request.form['firstname'],
        lastname = request.form['lastname'],
        img_url = request.form['img_url'] or None
    )

    db.session.add(new_user_info)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(users_id):
    user = Users.query.get_or_404(users_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:users_id>/edit')
def users_edit(users_id):
    user = User.query.get_or_404(users_id)
    return render_template('users/edit.html', user = user)

@app.route('/users/<int:users_id>/edit', methods=["POST"])
def users_update(users_id):
    user = Users.query.get_or_404(users_id)
    user.firstname = request.form['firstname']
    user.lastname = request.form['lastname']
    user.img_url = request.form['img_url']

    db.session.add(user)
    db.session.commit()
    return redirect("/users")

@app.route('/users/<int:users_id>/delete', methods=["POST"])
def users_delete(users_id):
    user = Users.query.get_or_404(users_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

