# Model Deployment Tutorial

In this tutorial, we'll explore how to deploy pretrained models using Streamlit, Django, and Flask. This tutorial is designed for first-year students and aims to provide a basic understanding of networking concepts such as requests, responses, JSON, APIs, and the Fetch API in Python.

**Objectives:**

- Understand fundamental networking concepts.
- Learn to build APIs and endpoints using Flask and Django.
- Create a website for model deployment using Streamlit.


### Setting up the environment

First install `virtualenv` by running : 

```
pip install virtualenv
```

Then, create a virtual enviroment: 

```
virtualenv env
```

After virtual env is created. Then, following command to activate it: 

```
source ./env/bin/activate
```

Then, install the requirements: 

```
pip install -r requirements.txt
```


## Flask

A basic flask app 

```python
# app.py

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_word():
    return "Hello, World"


if __name__ == "__main__":
    app.run(debug=True)

```

In order to run the flask app, run the following command 


```bash
python3 app.py # app.py file name
```


## TODO:

- Materials About, basic concepts of Networking
    - [ ] API, HTTP, JSON, HTTP Methods (GET, POST, ..,)
    - [x] apply these concepts in `Flask`.
    - [ ] Build a simple TODO APP.

- Fetch APIs: 
    - [ ] Looking for available APIs (ex. Github API)
    - [ ] Materials About: using the `requests` library, fetch website & APIs.

- ML Models:
    - [ ] Looking for pre-trainned models, to use in this tuto.
    - [ ] Work with different data type: text, images, json ...
