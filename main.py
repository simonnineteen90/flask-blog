from flask import Flask, render_template
import requests

app = Flask(__name__)


# API Request
def get_api_data():
    response = requests.get('https://api.npoint.io/43644ec4f0013682fc0d')
    response.raise_for_status()
    data = response.json()
    return data


@app.route('/')
def index():
    api_data = get_api_data()
    print(api_data[0])
    return render_template('index.html', data=api_data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def post(index):
    api_data = get_api_data()
    requested_post = None
    for blog_posts in api_data:
        if blog_posts["id"] == index:
            requested_post = blog_posts

    return render_template('post.html', post=requested_post)




if __name__ =="__main__":
    app.run(debug=True)
