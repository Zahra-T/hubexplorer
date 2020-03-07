from os.path import join, dirname
import functools
import easycli
import requests
import json

__version__ = '0.1.0'

def usernamecompleter(prefix, action, parser, parsed_args):
    pass

UsernameArgument = functools.partial(
    easycli.Argument,
    'username',
    help='Username',
    completer=usernamecompleter
)


class Repo(easycli.SubCommand):
    __command__ = 'repo'
    __aliases__ = ['r']
    __arguments__ = [
        UsernameArgument(),
    ]

    def __call__(self, args):
        username = args.username
        print(self.getrepos(username))
        return

    @staticmethod
    def getrepos(username):
        response = requests.get(url = f'https://api.github.com/users/{username}/repos')
        data = json.loads(response.text)
        repolist = []
        for o in data:
            repolist.append(o['name'])

        return ('{0}\'s repositories are:\n    {1}'.format(username, '\n    '.join(repolist)))


class HubExplorer(easycli.Root):
    __help__ = 'Easy github explorer'
    __completion__ = True,
    __arguments__ = [
        easycli.Argument(
            '-v', '--version',
            help='Show version'
        ),
        Repo,
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)

