#!/usr/bin/env python3
""" a Python function that lists all documents in a collection
Return an empty list if no document in the collection
"""
import pymongo


def list_all(mongo_collection):
    """ List all documents in a collection """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents if documents else []
