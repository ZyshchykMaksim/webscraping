# webscraping
Gets all the images from the site using modules: argparse, requests and BeautifulSoup


# arguments

    python imgs_scrapper.py -h

usage: imgs_scrapper.py [-h] [-o OUTPUTFILE] url


positional arguments:

  **url**                   - The address of website

optional arguments:

  **-h, --help**            - show this help message and exit
  
  **-o OUTPUTFILE, --outputfile** OUTPUTFILE                        - The name/path of the JSON output file

# example

    python imgs_scrapper.py https://www.habr.com -o data.json
