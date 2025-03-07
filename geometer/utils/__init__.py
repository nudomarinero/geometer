from typing import Generator, Iterable, TypeVar

from .indexing import normalize_index, posify_index, sanitize_index  # noqa: F401
from .math import (adjugate, det, hat_matrix, inv, is_multiple, is_numeric_dtype, matmul, matvec,  # noqa: F401
                   null_space, orth, outer, roots)

T = TypeVar("T")


def distinct(iterable: Iterable[T]) -> Generator[T, None, None]:
    """A simple generator that returns only the distinct elements of another iterable.

    Args:
        The iterable to filter.

    Yields:
        The distinct elements of the iterable.

    """
    seen = []
    for x in iterable:
        if x in seen:
            continue
        yield x
        seen.append(x)
