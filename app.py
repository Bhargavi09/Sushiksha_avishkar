from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/book')
def book():
    return render_template("book.html")
@app.route('/pygames')
def pygames():
    return render_template("pygames.html")
@app.route('/colorgame')
def colorgame():
    return render_template("colorgame.html")
@app.route('/Link1')
def Link1():
    return render_template("Link1.html")
@app.route('/Link2')
def Link2():
    return render_template("Link2.html")
@app.route('/hangman')
def hangman():
    return render_template("hangman.html")
   

if __name__ == '__main__':
    app.run()
