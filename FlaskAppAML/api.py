import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    '''<h1>wines</h1>'''
    return (
        f"Available Routes:<br/>"
        f"/api/v1/resources/wines/all<br/>"
        f"Available Searches:<br/>"
        f"/api/v1/resources/wines<br/>"
        f"/api/v1/resources/wines?country=Australia<br/>"
        f"/api/v1/resources/wines?country=US<br/>"
        f"/api/v1/resources/wines?country=Canada<br/>"
        f"/api/v1/resources/wines?country=Italy<br/>"
        f"/api/v1/resources/wines?country=France<br/>"
        f"/api/v1/resources/wines?country=Spain<br/>"
        f"/api/v1/resources/wines?country=Argentina<br/>"

    )


@app.route('/api/v1/resources/wines/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('wines.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_wines = cur.execute('SELECT * FROM wine;').fetchall()

    return jsonify(all_wines)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/wines', methods=['GET'])
def api_filter():
    query_parameters = request.args

    country = query_parameters.get('country')
    points = query_parameters.get('points')
    taster = query_parameters.get('taster_name')
    variety = query_parameters.get('variety')

    query = "SELECT * FROM wine WHERE"
    to_filter = []

    if country:
        query += ' country=? AND'
        to_filter.append(country)
    if points:
        query += ' points=? AND'
        to_filter.append(points)
    if taster:
        query += ' taster=? AND'
        to_filter.append(taster)
    if variety:
        query += ' variety=? AND'
        to_filter.append(variety)
    if not (country or points or taster or variety):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('wines.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()