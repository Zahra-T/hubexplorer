from os.path import join, dirname
import functools
import easycli
import requests
import json
import hubexplorer


__version__ = '0.1.0'


UsernameArgument = functools.partial(
    easycli.Argument,
    'username',
    help='Username',
)

OAuthToken = functools.partial(
        eacycli.Argument,
        'token', 'oauthtoken',
        help='OAuth2 token'
)

class Login(easycli.SubCommand):
    __command__ = 'login'
    __aliases__ = ['l']
    __arguments__ = [
            OAuthToken(),
    ]

class Repo(easycli.SubCommand):
    __command__ = 'repo'
    __aliases__ = ['r']
    __arguments__ = [
        UsernameArgument(),
    ]

    def __call__(self, args):
        username = args.username
        print(explorer.getrepos(username))
        return


class HubExplorer(easycli.Root):
    __help__ = 'Easy github explorer'
    __completion__ = True,
    __arguments__ = [
        easycli.Argument(
            '-v', '--version',
            help='Show version'
        ),
        Repo,
        Login,
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)

