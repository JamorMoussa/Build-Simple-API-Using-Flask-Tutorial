## Fetch API using `requests` library

### Use `get` Method

To fetch data from an API, you can use the `get` method provided by the `requests` library. This method sends a GET request to the specified URL and returns a response object.

```python
import requests as rq

# Send GET request to fetch all tasks
res = rq.get(f"http://10.1.10.195:5000/todo/api/v1.0/tasks")

# Print the response status code
print(res)

# Print the response content as JSON
print("response: ", res.json())
```

Output:
```
<Response [200]>
response:  {'count': 2, 'tasks': [{'description': 'some desc', 'done': False, 'id': 0, 'title': 'some title'}, {'description': 'desc 2', 'done': False, 'id': 1, 'title': 'title 2'}]}
```

### Use `get` with parameters

You can also pass parameters to the `get` method to filter the results. For example, to fetch a specific task by its ID:

```python
import requests as rq

# Send GET request with parameters
res = rq.get(f"http://10.1.10.195:5000/todo/api/v1.0/task", params={"id": 0})

# Print the response status code
print(res)

# Print the response content as JSON
print("response: ", res.json())
```

Output:
```
<Response [200]>
response:  {'task': [{'desc': 'some desc', 'done': False, 'id': 0, 'title': 'some title'}]}
```

### Use `post` Method

To add new data to the API, you can use the `post` method. This method sends a POST request with JSON data to the specified URL.

```python
import requests as rq

# Send POST request to add a new task
res = rq.post(
    f"http://10.1.10.195:5000/todo/api/v1.0/add", 
    json= {
        "title": "some title",
        "description": "some description",
        "done": False
    })

# Print the response status code
print(res)

# Print the response content as JSON
print("response: ", res.json())
```

Output:
```
<Response [200]>
response:  {'message': 'Task was successfully added.', 'status': 'success'}
```

### Use `delete` Method

To delete data from the API, you can use the `delete` method. This method sends a DELETE request with parameters to the specified URL.

```python
import requests as rq

# Send DELETE request to remove a task by ID
res = rq.get(
    f"http://10.1.10.195:5000/todo/api/v1.0/delete", params={"id": 0})

# Print the response status code
print(res)

# Print the response content as JSON
print("response: ", res.json())
```

Output:
```
<Response [200]>
response:  {'message': 'Task was successfully removed.', 'status': 'success'}
```
