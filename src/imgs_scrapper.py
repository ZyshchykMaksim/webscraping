'''
    Get all the images from the site using modules: argparse, requests and BeautifulSoup
    Author: Maksim Zyshchyk
    Email: amporioo@gmail.com
    Twitter: @zyshchykmaksim
'''

import sys
import argparse
import re
import json
import datetime
from requests import exceptions, get
from bs4 import BeautifulSoup


def main():
    url, outputfile = get_args()

    try:
        source = get(url).text
        imgUrls = get_url_images_in_text(source)
        data = {"site": url, "images": imgUrls}
        if outputfile is not None:
            print(str(datetime.datetime.now()) +
                  " - Outputting to file %s" % outputfile)
            toJSON(outputfile, data)
            print(str(datetime.datetime.now()) + " - Done!")
        else:
            print(data)

    except (exceptions.HTTPError, exceptions.ConnectionError, exceptions.Timeout, exceptions.RequestException) as httpEx:
        print(httpEx)
    except Exception as ex:
        print(ex)
    finally:
        sys.exit(0)


def get_args():
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
        description='The script extracts the links to images')
    parser.add_argument('url', type=str,
                        help='The address of website', )
    parser.add_argument('-o', '--outputfile', dest='outputfile',
                        help='The name/path of the JSON output file')

    args = parser.parse_args()

    return args.url, args.outputfile


def get_url_images_in_text(text):
    img_pattern = r'(?:http\:|https\:)?\/\/.*\.(?:jpg|gif|png|jpeg)'
    urls = []

    results = re.findall(
        img_pattern, text, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)

    for x in results:
        if x.startswith('http://') or x.startswith('https://'):
            urls.append(x)
        else:
            urls.append('http:' + x)

    return urls


def toJSON(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
