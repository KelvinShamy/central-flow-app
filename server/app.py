from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/task": {"origins": "http://localhost:4200"}})

@app.route("/", methods=['GET', 'POST'])
def home():
    return {"message": "Hello from Flask"}

@app.route("/task", methods=['GET', 'POST'])
def task():
    return {
        "message": "Tasks here",
        "tasks" : [
            {
                "name": "Task 1",
                "content": "This is the body of task 1"
            },
            {
                "name": "Task 2",
                "content": "This is the body of task 2"
            },
            {
                "name": "Task 3",
                "content": "This is the body of task 3"
            },
            {
                "name": "Task 4",
                "content": "This is the body of task 4"
            },
        ]
    }

if __name__ == '__main__':
    app.run(debug=True)
