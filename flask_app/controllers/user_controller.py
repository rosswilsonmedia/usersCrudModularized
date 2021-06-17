from flask import render_template, request, redirect

from flask_app import app
from ..models.user import User

@app.route('/users')
def user():
    users = User.get_all()
    print(users)
    return render_template('users.html', all_users=users)

@app.route('/users/new')
def new_user():
    return render_template('create_user.html')

@app.route('/users/<int:id>')
def show_user(id):
    data={
        'id':id
    }
    one_user=User.get_one(data)
    print(one_user)
    return render_template('show_user.html', user=one_user[0])

@app.route('/users/save', methods=['POST'])
def save_user():
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.save(data)
    return redirect('/users')

@app.route('/users/<int:id>/edit')
def edit_user(id):
    data={
        'id':id
    }
    one_user=User.get_one(data)
    print(one_user)
    return render_template('edit_user.html', user=one_user[0])

@app.route('/users/update', methods=['POST'])
def update_user():
    data={
        'id':request.form['id'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    print(data)
    User.update_user(data)
    return redirect('/users')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data={
        'id':id
    }
    User.delete_user(data)
    return redirect('/users')

