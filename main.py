from flask import Flask, jsonify, render_template, request
import json
import requests
import random

app = Flask(__name__)


stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]

@app.route('/')
def homie():
    with open('joke.json', encoding='utf-8') as c:
        json_data = json.load(c)
        num = random.randint(1, len(json_data))
        print("Number", num)    
        num2 = random.randint(1, len(json_data))
        num3 = random.randint(1, len(json_data))
        joo = json_data[num].get('body')
        joo2 = json_data[num2].get('body')
        joo3 = json_data[num3].get('body')
    return render_template('index.html', joke1=joo, joke2=joo2, joke3=joo3)
@app.route('/one')
def one():
     with open('oneline.json', encoding='utf-8') as d:
        json_data = json.load(d)
        num = random.randint(1, len(json_data))
        print("Number", num)    
        num2 = random.randint(1, len(json_data))
        num3 = random.randint(1, len(json_data))
        joo = json_data[num].get('setup')
        joop = json_data[num].get('punchline')
        joo2 = json_data[num2].get('setup')
        joo2p = json_data[num].get('punchline')
        joo3 = json_data[num3].get('setup')
        joo3p = json_data[num].get('punchline')
        return render_template('onel.html', joke1=joo, joke1p=joop, joke2=joo2, joke2p=joo2p, joke3=joo3, joke3p=joo3p)
    
@app.route('/s')
def home():
     response = requests.get("https://v2.jokeapi.dev/joke/Any")
     json_data = json.loads(response.text)

     return render_template('index.html'), #joke1=joke1)


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/majak')
def get_all_store_name():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run(port=5000)