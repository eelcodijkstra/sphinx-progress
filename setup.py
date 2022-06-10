from setuptools import setup, find_packages

setup(
    name='sphinx_progress',
    version='0.1.0',
    description='Progress logging for Sphinx-assessment in Jupyter Books',
    author='Eelco Dijkstra',
    author_email='eelco@infvo.nl',
    url='https://github.com/eelcodijkstra/sphinx-progress',
    packages=find_packages(include=['sphinx_progress', 'sphinx_progress.*']),
    license="MIT"
)