#!/usr/bin/env python3
""" Pagination project"""
from typing import Tuple


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
