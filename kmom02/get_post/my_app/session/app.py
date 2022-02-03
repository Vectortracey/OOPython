#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler

import json
import traceback
from flask import Flask, render_template, request
from bank import Bank


app = Flask(__name__)


bank = Bank()


@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/show_accounts")
def show_accounts():
    """
    accounts sida
    """
    return render_template("accounts.html", accs=bank.accounts)

@app.route("/addaccount", methods=["POST", "GET"])
def add_account():
    """
    lägg till accounts sida
    """
    if request.method == "POST":
        print(request.form)
        bank.add_account(request.form)
        bank.save_data()
    return render_template("add_account.html")

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
