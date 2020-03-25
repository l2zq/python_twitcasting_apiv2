#!/bin/env python3
import json
from typing import Optional
from urllib.parse import urlencode

from tc.auth import TCAuth, TCAppAuth, TCUserAuth

host = 'apiv2.twitcasting.tv'


class TCRequest():
    def __init__(self, method, url, body, headers):
        self.url = url
        self.body = body
        self.host = host
        self.method = method
        self.headers = headers


def make_req(auth: Optional[TCAuth], method: str, path: str, args=None) -> TCRequest:
    body = None
    hdrs = {
        'X-Api-Version': '2.0',
        'Accept-Encoding': 'gzip'
    }
    if auth:
        if isinstance(auth, TCAuth):
            hdrs['Authorization'] = auth.authorization
        else:
            raise TypeError('auth must be an instance of TCAuth')
    if args:
        if method in ('POST', 'PUT'):
            hdrs['Content-Type'] = 'application/json'
            body = json.dumps(args)
        else:
            args = urlencode(args)
            path = '%s?%s' % (path, args)
    return TCRequest(method, path, body, hdrs)

