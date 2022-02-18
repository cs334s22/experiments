from dotenv import load_dotenv
import requests
import os

def go():
    # Make sure to add a .env file with
    # KEY=<your_key>
    load_dotenv()
    key = os.getenv('KEY')

    # TODO: get jsons? from mongo db comments

    # TODO: check for attachments in those
        # TODO: check if the attachments linked come in pairs or some are one link, etc.

    # TODO: download the links from those attachments

        # TODO: check the types of documents

    pass




if __name__=='__main__':
    go()