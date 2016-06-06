from __future__ import absolute_import, division, print_function, unicode_literals  # noqa

from copy import copy
from contextlib import contextmanager
from werkzeug.local import LocalStack, LocalProxy


class Context(LocalStack):
    pass


def _lookup_context():
    top = _context_stack.top
    if top is None:
        raise RuntimeError('Working outside of browser context.')
    return top


def _copy_or_create_context():
    if _context_stack.top:
        return copy(_context_stack.top)
    else:
        return Context()


@contextmanager
def browser_context():
    context = _copy_or_create_context()
    _context_stack.push(context)
    try:
        yield
    finally:
        _context_stack.pop()


_context_stack = LocalStack()
context = LocalProxy(_lookup_context)
