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
        try:
            # check that page and page size are integers and are positive
            assert isinstance(page, int) and isinstance(page_size, int)
            assert page > 0 and page_size > 0
            page_indexes = index_range(page, page_size)
            start, stop = page_indexes
            all_data = self.dataset()
            return all_data[start: stop]
        except Exception as e:
            raise e

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> dict:
        """method that takes the same arguments
        (and defaults) as get_page and returns a dictionary"""
        data = self.get_page(page, page_size)
        start, stop = index_range(page, page_size)
        all_data = self.dataset()
        # total pages, next and prev page indexing
        prev_start = start - page_size
        prev_stop = start
        next_start = stop
        next_stop = stop + page_size
        total_pages = round(len(self.dataset()) / page_size)

        # check that next and prev pages exist
        if all_data[prev_start: prev_stop]:
            prev_page = page - 1
        else:
            prev_page = None
        if all_data[next_start: next_stop]:
            next_page = page + 1
        else:
            next_page = None
        return {"page_size": page_size if data else 0, "page": page,
                "data": data, "next_page": next_page,
                "prev_page": prev_page, "total_pages": total_pages}
