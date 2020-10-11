from flask import Flask, render_template
from card import *

app = Flask(__name__)

# MYSQL Handlers
# db = MYSQL database


@app.route("/", methods=["GET", "POST", "DELETE"])  # main card view page
def cardsView():
    return render_template(
        "index.html",
    )

@app.route("/addCard", methods=["GET", "POST", "DELETE"])  # add Card page
def addCard():
    return render_template(
        "addCard.html",
    )

# @app.route("/", methods=["GET", "POST", "DELETE"])  # main set view page
# def setsView():
#     return render_template(
#         "setView.html",
#     )

# @app.route("/addSet", methods=["GET", "POST", "DELETE"])  # add set page
# def addSet():
#     return render_template(
#         "addSet.html",
#     )

if __name__ == "__main__":
    debug = True
    app.run(debug=debug)
