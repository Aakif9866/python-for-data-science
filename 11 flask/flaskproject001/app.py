# this is the minimal code  to start a server 

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello world"

# @app.route('/home')
# def hello_home():
#     return "hello from homepage"

# rendering html

# to render html directly -> create templates folder and use it 
# to create a route use render_template("file_name")
@app.route('/home')
def hello_home():
    return render_template("test.html")
@app.route('/home/test')
def test_home():
    return redirect(url_for("hello_home")) # redirecting successfully
            # this above concept is routing 
@app.route('/test2')
def test2_home():
    return render_template("test2.html")
            


@app.route('/<name>')
def hello_name(name):
    return f"hello {name}"

if __name__ == '__main__':
    app.run(debug=True)
# basic
# routing
# requirements -> pip freeze > requirements.txt -> to share your project with someone
# rendering html
# mini flask project