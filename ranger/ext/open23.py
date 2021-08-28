# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from __future__ import absolute_import

from contextlib import contextmanager

from ranger import PY3


# COMPAT: We use the pattern of opening a file differently depending on the
#         python version in multiple places. Having calls to open in multiple
#         branches makes it impossible to use a with-statement instead. This
#         contextmanager hides away the lack of an errors keyword argument for
#         python 2 and is now preferred. This can be safely dropped once we
#         ditch python 2 support.
# TODO: The unspecified-encoding lint should only be disabled for the Python 2
#       case but Pylint is failing to parse the second disable properly.
# pylint: disable=too-many-arguments,unspecified-encoding
@contextmanager
def open23(
    file,
    mode="r",
    buffering=-1,
    encoding="UTF-8",
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
):
    if PY3:
        fobj = open(
            file=file,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            newline=newline,
            closefd=closefd,
            opener=opener,
        )
    else:
        if buffering is None:
            fobj = open(name=file, mode=mode)
        else:
            fobj = open(name=file, mode=mode, buffering=buffering)
    try:
        yield fobj
    finally:
        fobj.close()
