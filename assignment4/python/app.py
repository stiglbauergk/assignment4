#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, template_folder='html')
client = MongoClient('mongo')
db = client.KillCounter

#Connect to and display database
@app.route('/', methods=['GET', 'POST'])
def gamers():


    if request.method == 'POST':

        id = list(request.form.keys())[0]
        cmd = request.form[id]

        if cmd == 'add':

            return redirect(url_for("create"))

        elif cmd == 'delete':

            rcd = db.gamers.find_one_and_delete({'_id': ObjectId(id)})
            msg = f'Deleted {rcd["name"]}'

        elif cmd == 'update':

            return redirect(url_for("update", id=id))

    else:
        msg = ''

    gamers = list(db.gamers.find())

    try:
        n_kills = max(len(g['kills']) for g in gamers)
    except ValueError:
        n_kills = 0

    return render_template('list.html',
                           gamers=gamers,
                           msg=msg,
                           n_kills=n_kills)

# Add new gamer with screenname and # of kills
@app.route('/create', methods=['GET', 'POST'])
def create():


    if request.method == 'POST':

        name = request.form["name"]
        kills_text = request.form["kills"]

        kills = [float(kill) for kill in kills_text.split(',')]

        db.gamers.insert(dict(name=name, kills=kills))

        return redirect(url_for("gamers"))

    return render_template('create.html')

# Update gamer screen name or number of kills
@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':

        name = request.form["name"]
        kills_text = request.form["kills"]

        kills = [float(kill) for kill in kills_text.split(',')]

        db.gamers.update_one({'_id': ObjectId(request.args['id'])},
                               {'$set': {'name': name, 'kills': kills}})

        return redirect(url_for("gamers"))

    gamer = db.gamers.find_one({'_id': ObjectId(request.args['id'])})

    return render_template('update.html',
                           name=gamer['name'],
                           kills=(', ').join(str(kill) for kill in gamer['kills']))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
