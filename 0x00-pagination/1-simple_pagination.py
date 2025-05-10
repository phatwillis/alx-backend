#!/usr/bin/env python3
"""simple pagination"""

import csv

from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1,
                 page_size: int = 10) -> List[List]:
        """get the page requested using index logic of get index"""

        # check that page and page size are integers and are positive
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        try:
            page_indexes = index_range(page, page_size)
            start, stop = page_indexes
            all_data = self.dataset()
            return all_data[start: stop]
        except Exception as e:
            raise e
