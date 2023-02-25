import re
from stories import story
from flask import Flask, render_template, request


app = Flask(__name__)

print(story.template)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home")
def home_page():

    special_words = re.findall('\{[^\}]+\}', story.template)
    word_lst = [word.strip("{}") for word in special_words]

    return render_template("home.html", word_list=word_lst)


@app.route("/story", methods=["GET", "POST"])
def story_page():
    if request.method == 'POST':
        form_data = {}
        for key, value in request.form.items():
            form_data[key] = value

    return render_template("story.html", story=story.generate(form_data))


@app.route("/outline")
def story_outline():
    return render_template("outline.html", story=story.template)
