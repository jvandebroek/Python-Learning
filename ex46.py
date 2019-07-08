try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jonas',
    'url' : 'N/A',
    'version' : '0.1',
    'install_requires': ['Nothing'],
    'packages': ['None']
    'scripts': [],
    'name' : 'project name'
}

setup(**config)
