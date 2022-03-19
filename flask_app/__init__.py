# Is it ok to do my imports likes this? i.e. import flask modules/methods
# here, and then in files  that need them:
# from flask_app import session
from flask import Flask, render_template, redirect, request, session
from flask_bcrypt import Bcrypt

app: 'Flask' = Flask(__name__)
app.secret_key = '705e7ab7-e6c8-4776-89df-786c90a3023a'

bcrypt = Bcrypt(app)

DATABASE = 'login_and_registration_db'