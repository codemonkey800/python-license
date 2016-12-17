from os.path import dirname, join
from setuptools import find_packages, setup


def read(filename):
    return open(
        join(
            dirname(__file__),
            filename,
        ),
    ).read()


setup(
    name='license',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'click-completion',
        'click-didyoumean',
        'psutil',
        'requests',
        'requests-cache',
    ],
    py_modules=['license'],
    entry_points={
        'console_scripts': [
            'license=license.__main__:main',
        ],
    },

    # Package Metadata
    author='Jeremy Asuncion',
    author_email='jeremyasuncion808@gmail.com',
    description=('A command line app that fetches opensource licenses.'),
    long_description=read('README.md'),
    url='https://github.com/codemonkey800/python-license',
    license='MIT',
)
