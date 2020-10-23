import requests
from flask import Flask, redirect, render_template, request, url_for
import random

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/search', methods=["GET", "POST"])
def search():
    items =  request.args.get('mysearch')
    options = request.args.get('cle')
    resulte = 'wrong input, try to search again'
    resp = requests.get(f'https://rickandmortyapi.com/api/{options}').json()
    if items and options == "character":
        for i in range(35):
            resp = requests.get(f'https://rickandmortyapi.com/api/{options}?page={i}').json()
            for i in range(21):
                try:
                    if resp['results'][i]['name'].lower().startswith(items.lower()):
                        resulte = resp['results'][i]
                        return render_template('search.html', yoursearch=resulte, options=options, items=items)
                except IndexError as err:
                    print(err)
    elif options == "character":
        resulte = requests.get(f'https://rickandmortyapi.com/api/{options}?page={random.randint(0, 34)}').json()['results']
        return render_template('search.html', yoursearch=resulte, options=options)
    return render_template('search.html', yoursearch=resulte, options=options)


@app.route('/about-us')
def about_us():
    return render_template('about-us.html')


@app.route('/find-us')
def find_us():
    return render_template('find-us.html')


@app.route('/staff')
def stuff():
    return render_template('staff.html')


if __name__ == '__main__':
    app.run(debug=True)
