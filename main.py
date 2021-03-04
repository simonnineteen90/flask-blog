from flask import Flask, render_template
import requests

app = Flask(__name__)


# API Request
def get_api_data():
    response = requests.get('https://api.npoint.io/43644ec4f0013682fc0d')
    response.raise_for_status()
    data = response.json()[0]["body"]
    return data


@app.route('/')
def index():
    print(get_api_data())
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ =="__main__":
    app.run(debug=True)
