import json


def scheduled_on_wednesday(response):
    assert "Wednesday" in response.json()['schedule']['days']


def benjamin_in_show_archer(response):
    actors = []
    for person in response.json():
        actors.append(person['person']['name'])
    assert "H. Jon Benjamin" in actors


def pagination_works(response):
    assert len(response.json()) <= 250

def save_response(response, filename):
    with open(filename, 'w') as f:
        json.dump(response.json(), f)