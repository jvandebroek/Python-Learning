try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 47 project',
    'author': 'Jonas',
    'url' : 'N/A',
    'download url' : 'where to download',
    'author email' : 'my email',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name' : 'ex47'
}

setup(**config)
