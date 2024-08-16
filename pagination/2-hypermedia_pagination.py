#!/usr/bin/env python3
"""
This is the 1-simple_pagination module.
"""
import csv
from math import ceil
from typing import List, Tuple, Dict


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Checks the arguments and then returns the right page of the dataset.
        If the input arguments are out of range for the dataset, an empty
        list should be returned.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start, end = self.index_range(page, page_size)

        return dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing the following data about the
        hypermedia:

            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an int
        """
        hyper = {}
        page_data = self.get_page(page, page_size)
        hyper["page_size"] = len(page_data)
        hyper["page"] = page
        hyper["data"] = page_data

        total_pages = ceil(len(self.dataset()) / page_size)
        hyper["next_page"] = None
        if page < total_pages:
            hyper["next_page"] = page + 1

        hyper["prev_page"] = None
        if page > 1:
            hyper["prev_page"] = page - 1

        # Rounding up for the last page
        hyper["total_pages"] = total_pages

        return hyper
