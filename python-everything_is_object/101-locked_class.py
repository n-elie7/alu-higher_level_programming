#!/usr/bin/python3
"""Module that defines the locked class"""


class LockedClass:
    """LockedClass that prevents the dynamic creation of attributes"""
    __slots__ = ['first_name']
