# go to flask 1 14 minutes template inheritance
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# stop cookie interference
app.config['SECRET_KEY'] = 'd9e5d161aea7bdaae66380655b0334a7'
# add a dictionary within a list
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First blogs post content',
        'date_posted': 'March 17, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': '2nd blogs post content',
        'date_posted': 'March 18, 2018'
    },
    {
        'author': 'Jack Doe',
        'title': 'Blog Post 3',
        'content': '3nd blogs post content',
        'date_posted': 'March 121, 2018'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='title')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)
# another way of refreshing browser
if __name__ =='__main__':
    app.run(debug=True)
