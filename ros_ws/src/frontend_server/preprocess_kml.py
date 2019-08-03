#!/usr/bin/env python

"""
This script expects a 'static' folder to be in the same directory
and will download content into it.
"""

import sys
import urllib.request
from urllib.parse import urlparse
import os
from xml.dom import minidom

BRCMAP_KML_FILE = 'brcmap.kml'
CACHE_DIR = 'static'
HOSTNAME = 'www.gstatic.com'
LOCALHOST = 'localhost'

def eprint(*args, **kwargs):
    "Print to standard error"
    print(*args, file=sys.stderr, **kwargs)

def cache_content(link):
    "Cache content locally"
    path = urlparse(link).path
    dir = os.path.dirname(path)
    if dir:
        dir_to_create = CACHE_DIR + '/' + dir
        if not os.path.exists(dir_to_create):
            os.makedirs(dir_to_create)
    urllib.request.urlretrieve(link, CACHE_DIR + path)

def main(port):
    port = int(port)
    kml_doc = minidom.parse(BRCMAP_KML_FILE)
    links = kml_doc.getElementsByTagName('href')

    for link in links:
        originalLink = link.firstChild.data
        # print('Original link:', originalLink)
        try:
            cache_content(originalLink)
        except Exception as e:
            eprint("Failed caching", originalLink, '(', e, ')')
        # Update link in XML
        link.firstChild.data = originalLink.replace(HOSTNAME, LOCALHOST + ':' + str(port))
        # print('New link:', link.firstChild.data)

    print(kml_doc.toxml())

if __name__ == '__main__':
    main(sys.argv[1])
