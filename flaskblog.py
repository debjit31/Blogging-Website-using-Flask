from flask import Flask, render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Agnes Nielsen',
        'title' : 'Blog post1',
        'content' : 'First Blog Post',
        'date_posted' : 'April 21st, 2018'
    },
    {
        'author' : 'Debjit Chattopadhyay',
        'title' : 'Blog post2',
        'content' : 'Second Blog Post',
        'date_posted' : 'April 21st, 2018'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == "__main__":
    app.run(debug=True)
