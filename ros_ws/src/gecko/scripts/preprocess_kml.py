#!/usr/bin/env python

"""
This script expects a 'static' folder to be in the same directory
and will download content into it.

Run:

    python3 preprocess_kml.py original_brcmap.kml ../src/gecko/frontend_server/static 9090 > ../src/gecko/frontend_server/static/brcmap.kml

to generate a KML version where file are fetched from localhost:9090.
The script will download and cache the content under the static folder.
"""

import sys
import urllib.request
from urllib.parse import urlparse
import os
from xml.dom import minidom

HOSTNAME = 'www.gstatic.com'
LOCALHOST = 'localhost'

def eprint(*args, **kwargs):
    "Print to standard error"
    print(*args, file=sys.stderr, **kwargs)

def cache_content(link, out_dir):
    "Cache content locally"
    path = urlparse(link).path
    dir = os.path.dirname(path)
    if dir:
        dir_to_create = out_dir + dir
        if not os.path.exists(dir_to_create):
            os.makedirs(dir_to_create)
    urllib.request.urlretrieve(link, out_dir + path)

def main(src_file, out_dir, port):
    port = int(port)
    kml_doc = minidom.parse(src_file)
    links = kml_doc.getElementsByTagName('href')

    for link in links:
        originalLink = link.firstChild.data
        # print('Original link:', originalLink)
        try:
            cache_content(originalLink, out_dir)
        except Exception as e:
            eprint("Failed caching", originalLink, '(', e, ')')
        # Update link in XML
        link.firstChild.data = originalLink.replace(HOSTNAME, LOCALHOST + ':' + str(port) + '/static')
        # print('New link:', link.firstChild.data)

    print(kml_doc.toxml())

if __name__ == '__main__':
    main(src_file=sys.argv[1], out_dir=sys.argv[2], port=sys.argv[3])
