try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A game about space',
    'author': 'Jonas Vandebroek',
    'url' : 'N/A',
    'download url' : 'where to download',
    'author email' : 'jonasvandebroek@yahoo.com',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages': ['Game'],
    'scripts': [],
    'name' : 'Alien Mafia'
}

setup(**config)
