from flask import Flask
from vsearch import search4letters
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search():
    return str(search4letters(phrase='life, the universe, and everything',
                          letters='eiru,!'))

@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

app.run(debug=True)
