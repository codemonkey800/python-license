import json
import os.path as path
import re
import requests
import requests_cache
import tempfile

API_ROOT = 'https://api.github.com'
HEADERS = {
    'accept': 'application/vnd.github.drax-preview+json'
}

requests_cache.install_cache(
    path.normpath(tempfile.gettempdir() + '/license')
)


def __get(endpoint=''):
    '''Sends a request to an endpoint on the API root.'''
    r = requests.get(API_ROOT + endpoint, headers=HEADERS)
    if r.status_code != 200:
        raise RuntimeError(json.dumps(r.json(), indent=2))
    return r


def licenses(pattern=''):
    '''Retrieves licenses available and runs it through filters.'''
    r = __get('/licenses')
    lics = r.json()

    if pattern:
        def cb(lic):
            return (
                re.search(pattern, lic['key'], re.IGNORECASE) or
                re.search(pattern, lic['name'], re.IGNORECASE)
            )

        lics = list(filter(cb, lics))

    return lics


def license(name):
    '''Retrieves the contents of a license.'''
    if not name:
        raise ValueError('name must be a non-empty string!')
    r = __get('/licenses/{}'.format(name))
    return r.json()['body']
