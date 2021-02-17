from flask import Flask, request, render_template
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension

from stories import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "a-secret-key"
debug = DebugToolbarExtension(app)


@app.route('/')
def madlib_form():
    """Shows home page"""
    prompts = story.prompts
    return render_template('base.html', prompts=prompts)


@app.route('/story')
def story_page():
    """Displays user story"""
    story.generate(request.args)
    your_story = story.template

    return render_template("story.html", your_story=your_story)