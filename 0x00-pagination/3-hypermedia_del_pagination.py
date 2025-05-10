#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv

from typing import List, Dict


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """indexed items
        if the index is deleted, the next index can always be accessed
        because its stored."""
        try:
            dataset = self.dataset()
            assert index <= len(dataset) - 1
            end_index = index + page_size
            next_index = end_index
            resp_dict = {"index": index,
                         "next_index": next_index,
                         "page_size": page_size,
                         "data": [data for data in dataset[index: next_index]]}
            return resp_dict
        except Exception as e:
            raise e
