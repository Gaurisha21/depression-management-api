depression = [{
		"id": 1,
		"link": "https://youtu.be/yogdSYvaHV8"
	},{
		"id": 2,
		"link": "https://youtu.be/NHf56w1AmPw"
	},{
		"id": 3,
		"link": "https://youtu.be/XenNv9y4YZ8"
	},{
		"id": 4,
		"link": "https://youtu.be/lAdp3nT4BFA"
	},{
		"id": 5,
		"link": "https://youtu.be/NWBl81sipKs"
	},{
		"id": 6,
		"link": "https://youtu.be/OJfH0j6iF8I"
	},{
		"id": 7,
		"link": "https://youtu.be/MOiaSc38ZeI"
	},{
		"id": 8,
		"link": "https://youtu.be/0OFjkdmelOU"
	},{
		"id": 9,
		"link": "https://youtu.be/eAK14VoY7C0"
	},{
		"id": 10,
		"link": "https://youtu.be/8Su5VtKeXU8"
	},{
		"id": 11,
		"link": "https://youtu.be/_pYVQ_r-nrM"
	},{
		"id": 12,
		"link": "https://youtu.be/N4Jk9Cu3WM8"
	},{
		"id": 13,
		"link": "https://youtu.be/d-RcOuZ3I4E"
	},{
		"id": 14,
		"link": "https://youtu.be/DQC2eRUilUM"
	}
]

import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Suggestions to deal with Depression api</h1>
<p>A prototype API for providing solutions to deal with depression.</p>'''


@app.route('/api/depression/all', methods=['GET'])
def api_all():
    return jsonify(depression)


@app.route('/api/depression/random', methods=['GET'])
def api_id():
    results = []
    r = random.randint(1,14)
    # r0 = str(r)
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for depress in depression:
        if depress['id'] == r:
            results.append(depress)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
if __name__ == "__main__":
    app.run(debug = True, use_reloader=False)