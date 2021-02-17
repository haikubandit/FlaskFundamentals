from flask import Flask, request, render_template
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension

import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "a-secret-key"
debug = DebugToolbarExtension(app)



# @app.route('/')
# def madlib_form():
#     """Shows home page"""

#     prompts = story.prompts
#     return render_template('base.html', prompts=prompts)


@app.route("/")
def ask_story():
    """Show list-of-stories form."""

    return render_template("base.html", stories=stories.values())

@app.route("/questions")
def ask_questions():
    """Generate and show form to ask words."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("questions.html",
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)

# @app.route('/story')
# def story_page():
#     """Displays user story"""

#     text = story.generate(request.args)

#     return render_template("story.html", text=text)

@app.route("/story")
def show_story():
    """Show story result."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html",
                           title=story.title,
                           text=text)