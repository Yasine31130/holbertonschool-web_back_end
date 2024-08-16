#!/usr/bin/env python3
"""
This is the 9-insert_school module
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs and
    returns its ID.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
