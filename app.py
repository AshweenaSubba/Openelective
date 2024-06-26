from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Home.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)