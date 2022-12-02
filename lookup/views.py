from django.shortcuts import render


def home(request):
    import json
    # pip install requests
    import requests

    api_request = requests.get(
        'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=22302&distance=5&API_KEY=D969EC86-37FB-4820-8E23-82CD2DE0908C')

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = f'Error: {e}'
    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
