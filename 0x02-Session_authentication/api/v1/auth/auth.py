#!/usr/bin/env python3
"""
manages API authentication
"""


from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ manages API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path is in list of excluded paths
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if path[:p.find('*')] in p[:p.find('*')]:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns authorization header
        """
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None
        """
        return None

    def session_cookie(self, request=None):
        """Returns cookie value from request
        """
        if request:
            return request.cookies.get(getenv('SESSION_NAME'))
