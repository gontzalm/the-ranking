from flask import Response
from bson import json_util

def json_response(data):
    """ Process data with bson serializer to avoid ObjectID to string errors in flask."""
    return Response(
        json_util.dumps(data),
        mimetype='application/json'
    )

def parse_pull(pull):
    """TODO Parse GitHub API pull item"""
    pass