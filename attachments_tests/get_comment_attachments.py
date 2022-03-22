'''
You will need a folder named 'comments', one named 'related_response', and one named 'downloads'
You will also need a .env file containing 'KEY=<YOUR_KEY>' as this makes requests to regulations.gov

Your virtual environment must also have:
    PyMongo: pip install pymongo
    dotenv: pip install python-dotenv

Make sure to update your .gitignore to include:
    comments
    related_response
    downloads

Otherwise, you might accidentally upload all of the files that are created
'''

import json
import os
import requests
import urllib
from dotenv import load_dotenv
from pymongo import MongoClient

# MongoDB configs
uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(uri)
db = client.mirrulations
comments = db.comments

# Requests configs
load_dotenv()
params = { 'api_key': os.getenv('KEY') }


def get_comments():
    '''
    Save the comments from the database, as jsons.
    '''
    # The limit 10 is just so we don't check everything in the database
    for count, comment in enumerate(comments.find({}, 
                            {"data.id": 1, "data.relationships.attachments.links.related" : 1}).limit(10)):
        with open(f'comments/comment_{count}.json', 'w') as file:
            # Ideally we will just be sending this json, for now we save to disk
            file.write(json.dumps(comment, default=str))


def get_download_response(read_dir, write_dir):
    '''
    Makes a request to the related link from a comment. 
    The response from this contains the links for the files to be downloaded.
    '''
    for filename in os.listdir(read_dir):
        related_file_path = os.path.join(read_dir, filename)
        with open(related_file_path, 'r') as comment_related:
            data = json.load(comment_related)
            related = data['data']['relationships']['attachments']['links']['related']
            response_from_related = requests.get(related, params=params)
            with open(f'{write_dir}/response_{filename[:-5]}.json', 'w') as related_response_file: # need a better way to name the files
                related_response_file.write(json.dumps(response_from_related.json())) # This is what contains the links to download the actual attachment


def download_attachments(read_dir, write_dir):
    '''
    Make requests to regulation.gov to download the files from the the related responses.

    NOTE: many of the files are the same document just in a different format. For example, there
    may be a pdf and .doc file, but they are the same document. 

    Valid file types include: bmp, docx, gif, jpg, jpeg, pdf, png, pptx, rtf, sgml, tif, tiff, txt, wpd, xlsx, xml.
    See regulations.gov (click comment and above the file upload it shows valid file types)
    '''
    for filename in os.listdir(read_dir):
        related_file_path = os.path.join(read_dir, filename)
        with open(related_file_path, 'r') as related_response:
            data = json.load(related_response)
            downloads = data['data'][0]['attributes']['fileFormats']
            for i,download in enumerate(downloads):
                urllib.request.urlretrieve(download['fileUrl'], f'{write_dir}/download_{filename[:-5]}_{i}.{download["format"]}')

                # TODO: this uses requests, but there were issues with writing the file.
                # response = requests.get(download['fileUrl'])
                # with open(f'{write_dir}/download_{filename[:-5]}_{i}.{download["format"]}', 'w') as download: 
                #     download.write(response.content)


if __name__ == '__main__':
    get_comments()
    get_download_response('comments', 'related_response')
    download_attachments('related_response', 'downloads')
