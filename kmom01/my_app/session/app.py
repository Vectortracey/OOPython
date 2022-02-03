#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler

import json
import traceback
from flask import Flask, render_template
from person import Person


app = Flask(__name__)

persons_json = json.load(open("static/data/person.json", encoding="utf-8"))
persons = []

for i in persons_json:
    persons.append(Person.create_from_json(i))

person1 = Person("sven", 10000 "SavingAccount")

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html", i=persons[0], person=Person, person1=person1)

@app.route("/redovisning")
def show_redovisning():
    """
    redovisning sida
    """
    return render_template("redovisning.html")

@app.route("/about")
def show_about():
    """
    about sida
    """
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)
