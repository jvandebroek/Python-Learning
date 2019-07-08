try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jonas',
    'url' : 'N/A',
    'download url' : 'where to download',
    'author email' : 'my email',
    'version' : '0.1',
    'install_requires': ['nose'],
    'packages': ['main'],
    'scripts': [],
    'name' : 'projectname'
}

setup(**config)
