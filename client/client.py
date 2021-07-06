import click
import requests
from requests.exceptions import ConnectionError
import json


@click.command()
@click.option("--host", default="localhost", help="Server address(default=localhost)")
@click.option("--port", default="5000", help="Server port(default=5000)")
@click.option("--action", default="", help="CREATE to create task and GETSTATUS or GETRESULT to get status or result")
@click.option("--type", default="", help="REVERSE or REPLACE")
@click.option("--text", default="", help="text of yor task")
@click.option("--id", default="", help="task id")
def main(host, port, action, type, text, id):
    if action == "CREATE":
        create_task(host, port, type, text)
    elif action == "GETSTATUS":
        get_status(host, port, id)
    elif action == "GETRESULT":
        get_result(host, port, id)


def create_task(host, port, type_, text):
    try:
        req = requests.post(f"http://{host}:{port}/tasks", json={"type": type_, "text": text})
        if req.status_code != 200:
            print(req.json())
        else:
            print(req.content)
    except ConnectionError:
        print("invalid address")


def get_status(host, port, id_):
    ans = requests.get(f"http://{host}:{port}/tasks/{id_}").content.decode()
    ans = json.loads(ans)
    print(f"status: {ans.get('status')}")


def get_result(host, port, id_):
    ans = requests.get(f"http://{host}:{port}/tasks/{id_}").content.decode()
    ans = json.loads(ans)
    print(f"result: {ans.get('result')}")


if __name__ == '__main__':
    main()