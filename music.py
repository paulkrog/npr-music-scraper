#!/usr/bin/env python3

import webbrowser as wb
import requests
from lxml import html
import re
import pprint as pp

if __name__ == "__main__":
    pp.pprint("---GETting HTML from npr.org---")
    resp = requests.get(
        "http://www.npr.org/programs/all-things-considered/")
    tree = html.fromstring(resp.content)
    # get titles
    song_wrappers = tree.find_class("song-meta-wrap")
    queries = []
    for wrapper in song_wrappers:
        queries.append(" ".join((wrapper.text_content()).split()))

    for query in queries:
        wb.open_new_tab("http://youtube.com/results?search_query=" + query)
    pp.pprint("---Check your browser batch---")
