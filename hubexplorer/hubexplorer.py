import requests
import json

github = 'https://api.github.com'

def getrepos(username):
    response = requests.get(url = f'{github}/users/{username}/repos')
    data = json.loads(response.text)
    repolist = []
    for o in data:
        repolist.append(o['name'])

    return ('{0}\'s repositories are:\n    {1}'.format(username, '\n    '.join(repolist)))

def authentication(username, oauthtoken):
    response = requests.get(url = github,
                            headers=f'Authorization: token {oauthtoken}')
    data = json.loads(response.text)
    return data

def createrepo(info):
    jsondata = json.dumps(info)
    response = requests.post(f'{github}/user/repos', json=jsondata)
    data = json.loads(response.text)
    return data
