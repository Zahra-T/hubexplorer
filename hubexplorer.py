
    def getrepos(self, username):
        response = requests.get(url = f'https://api.github.com/users/{username}/repos')
        data = json.loads(response.text)
        repolist = []
        for o in data:
        repolist.append(o['name'])

        return ('{0}\'s repositories are:\n    {1}'.format(username, '\n    '.join(repolist)))

