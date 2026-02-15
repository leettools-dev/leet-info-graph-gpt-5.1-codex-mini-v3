class JWTError(Exception):
    """Simple JWT error used by the project tests.

    This is a minimal replacement for `jose.JWTError` to avoid adding
    an external dependency in the test environment.
    """
    pass

from . import jwt  # expose jwt submodule at package level
