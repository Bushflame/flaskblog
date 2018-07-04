# go to flask 1 14 minutes template inheritance
from flask import Flask, render_template
app = Flask(__name__)

# add a dictionary within a list
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First blog post content',
        'date_posted': 'March 17, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': '2nd blog post content',
        'date_posted': 'March 18, 2018'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='title')
