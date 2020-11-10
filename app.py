from flask import Flask, request, Response
import mariadb
import json
import random

app = Flask(__name__)

animal_list = ["Elephant", "Octopus", "Zebra", "Tuna", "Panda", "Lion", "Bear", "Snail"]

@app.route("/animals", methods = ["GET", "POST", "PATCH", "DELETE"])
def animals():
    if request.method == "GET":
        number = random.randrange(len(animals))
        random_animal = animal_list[number]
        seleciton = {"Random Animal": random_animal}
        return Response(json.dumps(seleciton, default=str), mimetype="application/json", status=200)
    elif request.method == "POST":
        return Response("You have successfully added Fish to the list. Well done!", mimetype="text/html", status=200)
    elif request.method == "PATCH":
        return Response("You have changed Snail to Gary. Excellent!", mimetype="text/html", status=200)
    elif request.method == "DELETE":
        return Response("You have removed Zebra from the list.", mimetype="text/html", status=200)


