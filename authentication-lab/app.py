from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {

  "apiKey": "AIzaSyAD4GfFEryVSOtmCwg8K31i9ARTCDnKPPQ",

  "authDomain": "yasmena1-d7852.firebaseapp.com",

  "projectId": "yasmena1-d7852",

  "storageBucket": "yasmena1-d7852.appspot.com",

  "messagingSenderId": "883793147528",

  "appId": "1:883793147528:web:8151bfd6c196e1badad13d",

  "measurementId": "G-NM1BS96RRV",
  "databaseURL": ""}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
           login_session['user'] = auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signin.html")



    



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
          login_session['user'] = auth.create_user_with_email_and_password(email, password)
          return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
    return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")



if __name__ == '__main__':
    app.run(debug=True)