#!/bin/env python3
import base64


class TCAuth():
    authorization = ''

    def __str__(self) -> str:
        return self.authorization

    def __repr__(self) -> str:
        return '<%s: %s>' % (self.__class__.__name__, self.authorization)


class TCAppAuth(TCAuth):
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorization = 'Basic ' + \
            base64.b64encode(('%s:%s' % (client_id, client_secret)).encode(
                'utf-8')).decode('utf-8')


class TCUserAuth(TCAuth):
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.authorization = 'Bearer ' + access_token
