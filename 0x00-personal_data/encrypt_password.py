#!/usr/bin/env python3
"""Encrypting passwords
"""
import bcrypt


def hash_password(password) -> str:
    """Hash a password before storage
    """
    value_bytes = password.encode('utf-8')
    salt_bytes = bcrypt.gensalt()
    # encrypted = bcrypt.hashpw(value_bytes, salt_bytes).decode('utf-8')
    encrypted = bcrypt.hashpw(value_bytes, salt_bytes)
    return encrypted
