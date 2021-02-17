from flask import Flask, request, render_template
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension

from stories import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('base.html')


@app.route('/story')
def story_page():
    """Greets and compliments a user"""
    # noun = request.args["noun"]
    # verb = request.args["verb"]
    # adjective = request.args["adjective"]
    # plural_noun = request.args["plural_noun"]
    index = story.prompts.index('place')
    story.prompts[index] = request.args["place"]
    your_story = story.template
    # nice_thing = choice(COMPLIMENTS)
    return render_template("story.html", your_story=your_story)