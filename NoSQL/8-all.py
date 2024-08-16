#!/usr/bin/env python3
"""
This is the 8-all module
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection, returns an empty list if no
    documents were found.
    """
    return list(mongo_collection.find())
