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
        easycli.Argument,
        'oauthtoken',
        help='OAuth2 token',
)

Name = functools.partial(
        easycli.Argument,
        'name',
        help='Repository name',
)

Description = functools.partial(
        easycli.Argument,
        '-d', '--description',
        help='Description',
        default='',
)

Private = functools.partial(
        easycli.Argument,
        '-p', '--private',
        help='Create a private repository',
        default=False,
)


class CreateRepo(easycli.SubCommand):
    __command__ = 'createrepo'
    __aliases__ = ['c']
    __arguments__ = [
            Name(),
            Description(),
            Private(),
    ]
    
    def __call__(self, args):
        info = {'name' : args.name, 
                'description' : args.description,
                'private' : args.private}
        print(hubexplorer.createrepo(info))

class Login(easycli.SubCommand):
    __command__ = 'login'
    __aliases__ = ['l']
    __arguments__ = [
            OAuthToken(),
    ]

    def __call__(self, args):
        print(hubexplorer.login(args.token))

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
        CreateRepo
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)

