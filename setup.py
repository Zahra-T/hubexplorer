import re
from os.path import join, dirname
from setuptools import setup

with open(join(dirname(__file__), 'explorercli.py')) as f:
    version = re.match('.*__version__ = \'(.*?)\'', f.read(), re.S).group(1)

dependencies = [
    'easycli',
    'requests',
    'oauthlib',
    'requests_oauthlib',
]


setup(
    name='hubexplorer',
    version=version,
    py_modules=['explorercli', 'hubexplorer'],
    install_requires=dependencies,
    include_package_data=True,
    license='MIT',
    entry_points={
        'console_scripts':[
            'hubexplorer = explorercli:HubExplorer.quickstart',
        ]
    }
)

