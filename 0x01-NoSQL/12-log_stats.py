#!/usr/bin/env python3
"""Log stats"""
import pymongo


def get_nginx_stats():
    """ returns stats for nginx """
    client = pymongo.MongoClient()
    db = client["logs"]
    nginx_collection = db["nginx"]

    # Count the total number of documents in the collection
    count = nginx_collection.count_documents({})
    print(f"{count} logs")
    print("Methods:")

    # Count the number of documents with each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\t{method_count} with method={method}")

    # Count the number of documents with method=GET and path=/status
    get_status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"\t{get_status_count} with method=GET and path=/status")

get_nginx_stats()
