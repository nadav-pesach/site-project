from flask import Flask, render_template, url_for, request, redirect
import requests


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
    if items:
        for i in range(20):
            if resp['results'][i]['name'].lower().startswith(items.lower()):
                resulte = resp['results'][i]
        return render_template('search.html', yoursearch=resulte)
    else:
        resulte = resp
    return render_template('search.html', yoursearch=resulte)


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
