"""
raised exceptions
"""

class Error(Exception):
    """User defined class for custom exceptions"""


class NoIndexValue(Error):
    """Raised when cannot find index because the list is empty or choice out \
    of range"""


class ValueNotFound(Error):
    """
    No matching value to the input found in the list
    """
