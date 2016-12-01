from os.path import dirname, join
from setuptools import setup


def read(filename):
    return open(
        join(
            dirname(__file__),
            filename,
        ),
    ).read()


setup(
    name='license',
    version='1.0',
    description=('A command line app that fetches open '
                 'source licenses from https://opensource.org.'),
    author='Jeremy Asuncion',
    author_email='jeremyasuncion808@gmail.com',
    url='https://gitlab.com/codemonkey800/python-license',
    license='MIT',
    py_modules=['license'],
    long_description=read('README.md'),
    entry_points={
        'console_scripts': [
            'license=license:main',
        ],
    },
)
