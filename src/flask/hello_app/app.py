from flask import Flask, request, jsonify



app = Flask(__name__)



@app.route("/", methods=["GET"])
def hello_word():
    return "Hello, World"


@app.route("/hello/<username>", methods=["GET"])
def hello_user(username):
    return f"Hello, {username}"


@app.route("/hello/", methods=["GET"])
def hello_user_1():
    username = request.args.get("user")
    return f"Hello, {username}"


@app.route('/post/', methods=['POST'])
def post_data():

    '''
        send: { "name": "moussa" }
    '''

    data = request.json

    name = data["name"]
    return f"you name is {name}" 


@app.route('/method/', methods=['GET', 'POST'])
def method_example():

    if request.method == "GET":
        return jsonify({"method": "GET"})
    
    if request.method == "POST":
        return jsonify({"method": "POST"})
    



if __name__ == "__main__":
    app.run(debug=True)