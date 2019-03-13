import os
import json

_HERE = os.path.realpath(os.path.dirname(__file__))

with open(os.path.join(_HERE, 'summary.json')) as h:
    SUMMARY = json.load(h)

with open(os.path.join(_HERE, 'csv_links_response.txt')) as h:
    CSV_LINKS_RESPONSE_TEXT = h.read()
