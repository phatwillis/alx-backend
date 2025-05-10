#!/usr/bin/env python3
"""Here I write a function named index_range that takes
two integer arguments page and page_size.
The function should return a tuple of size two
containing a start index and an end index corresponding
to the range of indexes to return in a list for those
particular pagination parameters."""

def index_range(page: int, page_size: int) -> tuple:
    """the function itself"""

    """set page limit for each page and end index
    end index is simply last index for that
    page alone. e.g a record with 2 pages and page limit of 10
    will have indexes 10 - 20 and end index is 20"""
    end_index = int(page_size * page)
    page_limit = page_size
    start_index = int(end_index - page_limit)
    page_range = start_index, end_index

    return page_range


