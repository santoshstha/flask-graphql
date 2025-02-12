from functools import wraps
from graphql import GraphQLError


def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise GraphQLError(str(e))
    return wrapper
