#!/usr/bin/env python3
""" a Python script that provides some stats about
Nginx logs stored in MongoDB:

Database: logs
Collection: nginx """


def log_stats(logs, nginx):
    x = logs.nginx.count()
    method_get = logs.nginx.count({"method": "GET"})
    method_post = logs.nginx.count({"method": "POST"})
    method_put = logs.nginx.count({"method": "PUT"})
    method_patch = logs.nginx.count({"method": "PATCH"})
    method_delete = logs.nginx.count({"method": "DELETE"})
    status = logs.nginx.count({$and: [{"method": "GET"}, {"path": "/status"}]})
    return "{} logs".format(x)"\n""Methods:\n\tmethod GET: {}".format(method_get)"\n\tmethod POST: {}".format(method_post)"\n\tmethod PUT: {}".format(method_put)"\n\tmethod PATCH: {}".format(method_patch)"\n\tmethod DELETE: {}".format(method_delete)"\n{} status check".format(status)
