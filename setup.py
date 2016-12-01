from distutils.core import setup

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
    entry_points={
        'console_scripts': [
            'license=license:main',
        ],
    },
)
