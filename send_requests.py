import requests

API_ADDRESS = "http://localhost:5555/todos"


def get_todos():
    r = requests.get(API_ADDRESS)
    return r.json()


def add_todo(todo_title):
    requests.post(API_ADDRESS, json={"title": str(todo_title)})


def delete_todo(todo_id):
    requests.delete(f"{API_ADDRESS}/{todo_id}")


def main():
    num_posts = 550
    for i in range(num_posts):
        add_todo(i)
        get_todos()

    todos = get_todos()
    for t in todos:
        delete_todo(t["id"])
        get_todos()


if __name__ == "__main__":
    main()
