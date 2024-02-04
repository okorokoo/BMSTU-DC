import pickle
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()
statistics = {u['id']: {
    'id': u['id'],
    'username': u['username'],
    'email': u['email'],
    'posts': 0,
    'comments': 0,
} for u in users}

posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()

for post in posts:
    statistics[post['userId']]['posts'] += 1

statistics = {u['email']: u for u in statistics.values()}

for comment in comments:
    if comment['email'] in statistics:
        statistics[comment['email']]['comments'] += 1

statistics = list(statistics.values())

response = requests.post('https://webhook.site/35c6d35f-9eea-4e47-93a9-e955c2905413', json={"statistics": statistics})
with open("solution.pickle", 'wb') as f:
    pickle.dump(response, f)
