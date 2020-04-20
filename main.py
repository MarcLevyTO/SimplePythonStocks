import json

items = json.loads(
    '[{"id": 1, "text": "Item 1"}, {"id": 2, "text": "Item 2"}]')

for item in items:
    print(item['text'])


def greet(greeting, name):
    """Returns a greeting

    Arguments:
        greeting {string} -- greet word
        name {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return f'{greeting} {name}'
