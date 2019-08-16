import requests
import json

from pprint import pprint


def get_client():
    url = 'https://jsonplaceholder.typicode.com/todos/1'

    r = requests.get(
        url=url
    )

    return r.json()


if __name__ == '__main__':
    pprint(get_client())
