import requests
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


github = 'https://api.github.com'

def getrepos(username):
    response = requests.get(url = f'{github}/users/{username}/repos')
    data = json.loads(response.text)
    repolist = []
    for o in data:
        repolist.append(o['name'])

    return ('{0}\'s repositories are:\n    {1}'.format(username, '\n    '.join(repolist)))

def authentication(username, oauthtoken):
    client_id = username
    client_secret = oauthtoken
    auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=f'{github}/user', auth=auth)
    return token
#318199a1a806247bc306e80cc051269a998a23d0
def createrepo(info):
    jsondata = json.dumps(info)
    response = requests.post(f'{github}/user/repos', json=jsondata)
    data = json.loads(response.text)
    return data
