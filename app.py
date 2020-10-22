from flask import Flask, render_template, url_for, request
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    # item = request.form.get('mybooks')
    # resulte = requests.get(f'')
    return render_template('search.html')

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