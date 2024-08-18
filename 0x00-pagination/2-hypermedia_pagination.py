#!/usr/bin/env python3
""" Pagination project"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Gets start and end indices of data
        - Args:
            page (int): page to look for information
            page_size (int): size of each page
        - Return: tuple of size two containing a start and end index
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retrieves dataset for specific page
        - Args:
            - page (int): page to look for information
            - page_size (int): size of each page
        - Return: the appropriate page of dataset (the correct list of rows)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Gets page data plus info to next and prev pages
        - Args:
            - page (int): page to look for information
            - page_size (int): size of each page
        - Return: a dictionary containing the following key-value pairs:
            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page
            - next_page: number of the next page, None if no next page
            - prev_page: number of the previous page, None if no previous page
            - total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        prev_page, next_page = None, None
        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1
        page_data = self.get_page(page, page_size)
        response = {'page_size': len(page_data),
                    'page': page,
                    'data': page_data,
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': total_pages}
        return response
