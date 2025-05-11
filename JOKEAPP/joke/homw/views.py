# jokes/views.py
import requests
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    # Optional: set the category — could be 'Any', 'Programming', etc.
    category = 'Any'

    # Call the JokeAPI
    url = f'https://v2.jokeapi.dev/joke/{category}?type=single,twopart'
    response = requests.get(url)
    data = response.json()

    # Prepare joke object to pass to the template
    if data.get('type') == 'twopart':
        joke = {
            'setup': data.get('setup'),
            'punchline': data.get('delivery')
        }
    else:
        joke = {
            'setup': '',
            'punchline': data.get('joke')
        }

    return render(request, 'home.html', {'joke': joke})


def get_joke_json(request):
    url = 'https://v2.jokeapi.dev/joke/Any?type=single,twopart'
    response = requests.get(url)
    data = response.json()

    if data.get('type') == 'twopart':
        joke = {
            'setup': data.get('setup'),
            'punchline': data.get('delivery')
        }
    else:
        joke = {
            'setup': '',
            'punchline': data.get('joke')
        }

    return JsonResponse(joke)