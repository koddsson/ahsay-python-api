import requests
import xml.etree.ElementTree as ET

try:
    # Python 3
    from urllib.parse import urlparse, urlunparse, urlencode
except ImportError:
    # Python 2
    from urlparse import urlparse, urlunparse
    from urllib import urlencode


class AhsayAPI(object):
    def __init__(self, username, password, hostname):
        self.base_qs = {'SysUser': username, 'SysPwd': password}
        self.base_url = '{host}/obs/api/'.format(
            host=hostname)

    def call(self, action, **kwargs):
        parts = urlparse(self.base_url + action + '.do')
        qs = urlencode(dict(kwargs, **self.base_qs))
        url = urlunparse((parts[0], parts[1], parts[2], parts[3], qs, parts[5]))
        response = requests.get(url)
        root = ET.fromstring(response.text)
        if root.tag == 'err':
            raise Exception(root.text)
        return root
