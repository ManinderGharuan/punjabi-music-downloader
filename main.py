#!/usr/bin/env python3

from scrapers import get_data
from html_generator import html_generator


if __name__ == '__main__':
    data = get_data()
    html = html_generator.get_html(data)

    print("Writing Html file")

    with open('punjabi-songs.html', 'w') as foo:
        foo.write(html)