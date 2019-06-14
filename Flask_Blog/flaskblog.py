from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4ea6c53cb4ad5be39a23' #key for saving against cookie changes, forgery etc

posts = [
	{
		'author': 'Suyash Trivedi',
		'title': 'Blog Post 1',	
		'content': 'First post content',
		'date_posted': 'June 20, 2019'
	},

	{
		'author': 'Surekha Trivedi',
		'title': 'Blog Post 2',	
		'content': 'Second post content',
		'date_posted': 'June 27, 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/register")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
	app.run(debug=True)    