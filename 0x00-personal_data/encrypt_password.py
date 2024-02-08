#!/usr/bin/env python3
""" Check valid password & Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ expects one string argument name password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Implement an is_valid function that expects 2 arguments """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
