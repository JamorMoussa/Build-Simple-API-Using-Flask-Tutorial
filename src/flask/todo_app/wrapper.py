from flask import jsonify, request
import functools

def raise_key_error(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        response = {}

        try:
            response = func(*args, **kwargs)

        except KeyError as e:

            response =  jsonify({
                "erorr-type" : "keyword Error",
                "missing-keyword": str(e).replace("'", "")
            })

        return response
    
    return wrapper