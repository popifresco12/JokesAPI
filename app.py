from flask import Flask, request
import json
import requests
import random
from math import gcd
from pymongo import MongoClient

app = Flask(__name__)
uri = "mongodb+srv://popifresco12:1234@cluster0.iducd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client.test
coll = db.jokes

@app.route('/', methods=['GET'])
def get_joke():
    header = ', headers={"Accept":"application/json"}'
    chuck = 'https://api.chucknorris.io/jokes/random'
    dad = 'https://icanhazdadjoke.com/'

    lista = ["dad", "chuck"]
    doc = random.choice(lista)

    if doc == "chuck":
        url = chuck
        req = requests.get(url)
        response = req.content
        dict = json.loads(response)

        return dict['value']
        
    elif doc == "dad":
        url = dad + header
        req = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
        response = req.content
        dict = json.loads(response)

        return dict['joke']

@app.route('/Chuck', methods=['GET'])
def get_chuck():
    req = requests.get('https://api.chucknorris.io/jokes/random')

    response = req.content
    dict = json.loads(response)

    return dict['value']

@app.route('/Dad', methods=['GET'])
def get_dad():
    req = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})

    response = req.content
    dict = json.loads(response)

    return dict['joke']


@app.route('/', methods=['POST'])
def post_joke():
    args = request.args
    joke = args.get("joke")
    joke_json = [
        {"joke": joke}
    ]

    result = coll.insert_many(joke_json)
    print("Insertado con exito")
    return joke

@app.route('/', methods=['PUT'])
def update_joke():
    args = request.args
    joke = args.get("joke")
    num = args.get("number")

    result = coll.update_one({"number": num}, {"$set": {"joke": joke}})
    print("Actualizad con exito")
    return joke

@app.route('/', methods=['DELETE'])
def delete_joke():
    args = request.args
    num = args.get("number")
    joke_json = {"number": num}
    

    result = coll.delete_one(joke_json)
    print("Number of documents deleted: ", result.deleted_count)
    return "num"



@app.route('/numbers', methods=['GET'])
def get_numbers():
    args = request.args
    num = args.get("numeros")

    lista = num.split(",")
    lcm = 1
    
    for i in lista:
        i = int(i)
        lcm = lcm*i//gcd(lcm, i)

    return str(lcm)

@app.route('/number', methods=['GET'])
def get_number():
    args = request.args
    num = args.get("numero")

    num = int(num)
    num = num + 1

    return str(num)


if __name__ == '__main__':
    app.run(debug=True)

