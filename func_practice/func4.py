#/usr/bin/env python3
"""Author: Robert Spring | Learning about functions"""

def greet(msg, name="Slappy"):
    """This sets a default value for name,
    if it's not provided"""
    print(f"Hello {name}, {msg}")

greet("how's it going?")
