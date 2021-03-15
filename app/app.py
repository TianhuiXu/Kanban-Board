import os

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

# create the flask application
app = Flask(__name__)
file_path = os.path.abspath(os.getcwd()) + "/kanban.db"

# configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# app.config['DEBUG'] = True
db = SQLAlchemy(app)


# create the Todo table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Integer)


# commit the table to the database
db.create_all()
db.session.commit()


# view for the index page
@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=0).all()
    complete = Todo.query.filter_by(complete=1).all()
    doing = Todo.query.filter_by(complete=2).all()
    return render_template('index.html', incomplete=incomplete, complete=complete, doing=doing)


# add todos according to the input form, return message with invalid input
@app.route('/addtodo', methods=['POST'])
def addtodo():
    text = request.form['Input_todo']
    if text == '':
        return jsonify(message='Add something to do!'), 400
    todo = Todo(text=text, complete=0)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))


# add doings according to the input form, return message with invalid input
@app.route('/adddoing', methods=['POST'])
def adddoing():
    text = request.form['Input_doing']
    if text == '':
        return jsonify(message='Add something that you are doing!'), 400
    todo = Todo(text=text, complete=2)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))


# add dones according to the input form, return message with invalid input
@app.route('/adddone', methods=['POST'])
def adddone():
    text = request.form['Input_done']
    if text == '':
        return jsonify(message='Add something that you have done!'), 400
    todo = Todo(text=text, complete=1)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))


# move todo or doing to done
@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = 1
    db.session.commit()

    return redirect(url_for('index'))


# move done or doing back to todo
@app.route('/backtodo/<id>')
def backtodo(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = 0
    db.session.commit()

    return redirect(url_for('index'))


# move todo to doing
@app.route('/todoing/<id>')
def todoing(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = 2
    db.session.commit()

    return redirect(url_for('index'))


# delete dones from
@app.route('/delete/<id>', methods=['Get'])
def del_item(id):
    item = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(item)
    db.session.commit()

    return redirect(url_for('index'))
