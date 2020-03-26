import re
from os.path import join, dirname
from setuptools import setup

with open(join(dirname(__file__), 'hubexplorer.py')) as f:
    version = re.match('.*__version__ = \'(.*?)\'', f.read(), re.S).group(1)

dependencies = [
    'easycli',
    'requests',
]


setup(
    name='hubexplorer',
    version=version,
    py_modules=['hubexplorer'],
    install_requires=dependencies,
    include_package_data=True,
    license='MIT',
    entry_points={
        'console_scripts':[
            'hubexplorer = hubexplorer:HubExplorer.quickstart',
        ]
    }
)

