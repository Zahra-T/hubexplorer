import requests
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
import os
import ast

github = 'https://api.github.com'

def getrepos(username):
    response = requests.get(url = f'{github}/users/{username}/repos')
    data = json.loads(response.text)
    repolist = []
    for o in data:
        repolist.append(o['name'])

    return ('{0}\'s repositories are:\n    {1}'.format(username, '\n    '.join(repolist)))

def authentication(username, oauthtoken):
    with open(os.path.expanduser(os.path.join('~', '.hubtokens.txt')), 'r+') as f:
        tokens = ast.literal_eval(f.read())
        tokens[username] = oauthtoken
        f.seek(0)
        f.write(str(tokens))

    return 'Token saved'

def createrepo(username, info):
    token = None
    with open(os.path.expanduser(os.path.join('~', '.hubtokens.txt')), 'r') as f:
        tokens = ast.literal_eval(f.read())
        token = tokens[username]

    response = requests.post(f'{github}/user/repos', json=info, auth=(username, token))
    data = json.loads(response.text)
    return data
