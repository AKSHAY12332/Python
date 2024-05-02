# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:05:45 2024

@author: Akshay Manthena
"""


from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.secret_key = os.urandom(32) #Generate 32 bytes of random data

#Simulated user database
users = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']
        
        #validate username and check for uniqueness
        if username in users and users[username]==password:
            session['username'] = username
            return redirect(url_for('welcome_home'))
        else:
            return render_template('login.html', message="Invalid Credentials. Please try again.")
        
    return render_template('login.html', message='')
    
@app.route('/register', methods=['GET','POST'])
def register():
    message = ''
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
    
        if username in users:
            message="Username already exists. Please choose another one."
        else:
            users[username] = password
            session['username'] = username
            return redirect(url_for('index'))

    if 'username' in session:
        return redirect(url_for('index'))

    return render_template('register.html', message=message)


@app.route('/welcome')
def welcome_home():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('index'))
    
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)