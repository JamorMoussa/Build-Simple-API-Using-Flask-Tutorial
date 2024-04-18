from flask import Flask, jsonify, request, Response
from todo import Todo
from wrapper import raise_key_error




app = Flask(__name__)

URL = "/todo/api/v1.0"

@app.route(f"{URL}/tasks", methods=["GET"])
def get_all_tasks() -> Response:
    
    res = {}

    res["tasks"] = [task.to_dict() for task in Todo.all()]
    res["count"] = Todo.count()
    
    return jsonify(res)

@app.route(f"{URL}/task", methods=["GET"])
def get_task_by_id() -> Response:

    res = {}
    
    id = request.args.get("id")
    if id is None:
        id = 0
    
    res["tasks"] = [Todo.get(id), ]
    
    return jsonify(res)

@app.route(f"{URL}/add", methods=["POST"])
@raise_key_error
def add_task():
    
    title = request.json["title"]
    desc = request.json["description"]
    done = bool(request.json["done"])
    
    Todo.create_task(title=title, desc=desc, done=done)
    
    return jsonify({
        "status": "success",
        "message": "Task was successfully added.",
    })

@app.route(f"{URL}/delete", methods=["GET"])
@raise_key_error
def delete_task_by_id():
    
    if (id := request.args.get("id")) is None: raise KeyError("id")
    
    Todo.delete_task_by_id(id)
    
    return jsonify({
        "status": "success",
        "message": "Task was successfully removed.",
    })


if __name__ == "__main__":

    Todo.create_task(title="some title", desc="some desc", done=False)
    Todo.create_task(title="title 2", desc="desc 2", done=False)

    app.run(debug=True)
