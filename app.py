from flask import Flask
from flask import render_template
from form import RegistrationForm , LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my secret key'

@app.route('/')

@app.route('/home')

def home():
    return render_template('home.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('signup.html' , title = 'Register' , form = form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html' , title = 'Login' , form = form)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__name__':
    app.run(debug=True)