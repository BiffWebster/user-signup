from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_signup():
    template = jinja_env.get_template('signup-page.html')
    return template.render()






@app.route("/", methods=['POST'])
def validate():
    name = request.form['username']
    password = request.form['password']
    match_pass = request.form['verify']
    email = request.form['email']
    template = jinja_env.get_template('signup-page.html')

    name_error = ""
    pass_error = ""
    match_error = ""
    email_error = ""


    if request.method == "POST":
        # validate username

        if not name:
            name_error = 'This field is required'
        elif len(name) < 3 or len(name) > 20 or " " in name:
            name_error = 'Username must be between 3 and 20 characters, no spaces allowed'



        # validate password

        if not password:
            pass_error = 'This field is required'
        if password == False and len(password) < 3 or len(password) > 20 or " " in password:
            pass_error='Password must be between 3 and 20 characters, no spaces allowed'
        else:
            pass_valid =True

            # validate matching passwords
        if match_pass != password:
            match_error = "Password does not match"

        # validate email

        if email.count("@") > 1 or email.count(".") > 1 or len(email) < 3 or len(email) > 20:
            email_error="Not a valid email"

        if not name_error and not pass_error and not match_error and not email_error:
            return welcome(name)
        else:
            return template.render(name=name, email=email, name_error=name_error, pass_error=pass_error, match_error=match_error, email_error=email_error)





@app.route("/welcome.html", methods=['GET', 'POST'])
def welcome(name):

    wel_template = jinja_env.get_template('welcome.html')

    return wel_template.render(name=name)


app.run()

