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
pip install -r requiremebs.txt
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