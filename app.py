from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Contact': u'6645045',
        'Name': u'John', 
        'done': False
    },
    {
        'id': 2,
        'Contact': u'94718432',
        'Name': u'Bill', 
        'done': False
    },
    {
        'id': 3,
        'Contact': u'33240531',
        'Name': u'Rin', 
        'done': False
    },
    {
        'id': 4,
        'Contact': u'22949005',
        'Name': u'Sarah', 
        'done': False
    },
    {
        'id': 5,
        'Contact': u'64328478',
        'Name': u'Mary', 
        'done': False
    },    
]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)