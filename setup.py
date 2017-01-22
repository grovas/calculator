try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple calculator',
    'author': 'Grovas',
    'url': 'https://github.com/grovas/calculator',
    'download_url': 'https://github.com/grovas/calculator',
    'author_email': 'arczir@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['calculator.py'],
    'scripts': [],
    'name': 'calculator'
}

setup(**config)
