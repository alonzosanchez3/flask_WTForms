from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from dotenv import load_dotenv
from wtforms.validators import DataRequired, Email, Length
import os
from flask_bootstrap import Bootstrap5

load_dotenv()

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")




'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def get_login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data, login_form.password.data)
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return success()
        else:
            return denied()
    return render_template('login.html', form=login_form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)
