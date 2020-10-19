from card_base import card_base
from types import new_class
from flask import Flask, render_template, request
from card import *

app = Flask(__name__)

# MYSQL Handlers
# db = MYSQL database

cards = []

@app.route("/", methods=["GET", "POST", "DELETE"])  # main card view page
def cardsView():
    # cards.append(1)
    # cards.append(2)

    if request.method == "POST":
        if "AddCard" in request.form:
            front = request.form["exampleInputEmail1"]
            back = request.form["exampleInputPassword1"]
            card_object = card_base(front, back)
            cards.append(card_object)
            for i in cards:
                print(i)
                print(i.frontside)
                print(i.backside)
        else:
            pass
    return render_template(
        "index.html",
        cards_array = cards
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
