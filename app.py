import requests
from flask import Flask, redirect, render_template, request, url_for
import random

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    resulte = []
    number = random.randint(0, 32)
    for i in range(number, number + 3):
        resulte += requests.get(
            f'https://rickandmortyapi.com/api/character?page={i}').json()['results']
    return render_template('index.html', yoursearch=resulte)


@app.route('/search', methods=["GET", "POST"])
def search():
    items = request.args.get('mysearch')
    options = request.args.get('cle')
    resulte = []
    if items and options == "character":
        resp = []
        for i in range(35):
            resp += requests.get(
                f'https://rickandmortyapi.com/api/{options}?page={i}').json()['results']
        for i in resp:
            try:
                if i['name'].lower().startswith(items.lower()):
                    resulte += [i]
            except IndexError as err:
                print(err)
        if resulte:
            return render_template('search.html', yoursearch=resulte, options=options, items=items)
        else:
            return render_template('index.html')
    elif options == "character":
        resulte = requests.get(
            f'https://rickandmortyapi.com/api/{options}?page={random.randint(0, 34)}').json()['results']
        return render_template('search.html', yoursearch=resulte, options=options)
    elif options == "episode":
        if not items:
            items = random.randint(1, 41)
        resp = requests.get(
            f'https://rickandmortyapi.com/api/episode/{items}').json()
        if 'error' in resp:
            return render_template('index.html')
        episode = resp['episode']
        name = resp['name']
        air_date = resp['air_date']
        resulte = []
        for person in resp['characters']:
            resulte += [requests.get(person).json()]
        return render_template('search.html', yoursearch=resulte, name=name, air_date=air_date, options=options, items=items, episode=episode)
    name_id = request.args.get('pictursearch')
    one = requests.get(f'https://rickandmortyapi.com/api/character/{name_id}').json()
    return render_template('search.html', name_id=one)


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
