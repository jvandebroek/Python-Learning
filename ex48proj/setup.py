try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Makes sentences and such',
    'author': 'Jonas',
    'url' : 'N/A',
    'download url' : 'where to download',
    'author email' : 'my email',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name' : 'ex48 lexicon'
}

setup(**config)
