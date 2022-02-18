from dotenv import load_dotenv
import requests
import os

def go():
    # Make sure to add a .env file with
    # KEY=<your_key>
    load_dotenv()
    key = os.getenv('KEY')

    server = 'https://api.regulations.gov/v4/'
    endpoint = 'dockets/'

    url = server + endpoint

    params = {'api-key':key}

    # TODO: get jsons? from mongo db comments
    try:
        def get_jsons():
            for json in jsons:
                pass

    response = requests.get(url, params=params, timeout=.001)
    response.raise_for_status()
    get_jsons(response.json())

    # TODO: check for attachments in those
        # TODO: check if the attachments linked come in pairs or some are one link, etc.

    # TODO: download the links from those attachments

        # Valid file types include: bmp, docx, gif, jpg, jpeg, pdf, png, pptx, rtf, sgml, tif, tiff, txt, wpd, xlsx, xml.
        # See regulations.gov (click comment and above the file upload it shows valid file type...)

    pass


if __name__=='__main__':
    go()