from card_base import card_base
from types import new_class
from flask import Flask, render_template, request
from card import *

app = Flask(__name__)


cards = []


@app.route("/", methods=["GET", "POST", "DELETE"])  # main card view page
def cardsView():

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

        elif "RemoveCard" in request.form:
            delete_val = request.form["deleteCard"]
            print(delete_val)
            i = 0
            for item in cards:
                if item.frontside == delete_val:
                    print(item.frontside)
                    break
                i += 1
            cards.pop(i)

    return render_template(
        "index.html",
        cards_array=cards
    )


@app.route("/addCard", methods=["GET", "POST", "DELETE"])  # add Card page
def addCard():
    return render_template("addCard.html"
                           )


if __name__ == "__main__":
    debug = True
    app.run(debug=debug)
