import requests


    def getrepos(self, username):
        response = requests.get(url = f'https://api.github.com/users/{username}/repos')
        data = json.loads(response.text)
        repolist = []
        for o in data:
        repolist.append(o['name'])

        return ('{0}\'s repositories are:\n    {1}'.format(username, '\n    '.join(repolist)))

    def authentication(self, username, oauthtoken):
        response = requests.get(url = 'https://api.github.com',
                                headers=f'Authorization: token {oauthtoken}')
        data = json.loads(response.text)
        print(data)
