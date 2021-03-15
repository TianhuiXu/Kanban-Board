## Welcome to Kanban!

### Introduction

This is an implementation of Kanban board - a task-management tool. With it, you are able to:
1. Create todos, doings, and dones
2. Change the status of an item
3. Delete an item once it's done
4. More features will come in soon!

### Structure of the project
The project is built using HTML and CSS for front end and Python Flask for backend.
### Run the program
To make the program run on your local machine, please follow the steps below:

1. create virtual env:
```bash
$ python3 -m venv .venv  
```
2. Activate Virtual Environment
```bash
$ source .venv/bin/activate         # for Linux & macOS
$ env\Scripts\activate            # for Windows
```
3. Install requirements
```bash
$ pip3 install -r requirements.txt
```
4. Locate the directory and run flask
```bash
$ cd app
$ export FLASK_APP=app.py
$ flask run
```

### Unit tests
#### Run unit tests
The project includes appropriate unit tests. These unit tests can be run using the following command (while in the project’s root directory):
```bash
$ python -m unittest discover test
```
#### Assess coverage of the unit tests
To assess the coverage of the test, you can follow the commands below (visit https://coverage.readthedocs.io/en/coverage-5.5/ for more information):

1. install coverage.py
```bash
$ pip install coverage
```
2. Use coverage run to run your test suite and gather data
```bash
$ coverage run -m unittest discover
```
3. Use coverage report to report on the results:
```bash
$ coverage report -m
Name                Stmts   Miss  Cover
---------------------------------------
app/__init__.py         0      0   100%
app/app.py             71      0   100%
tests/__init__.py      19      0   100%
tests/test_app.py      81      0   100%
---------------------------------------
TOTAL                 171      0   100%

```
4. use coverage html to get annotated HTML listings detailing missed lines:
```bash
$ coverage html
```
