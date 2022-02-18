'''
Allows clients to save 

Comments with attachments are not saved, with this (c_Attachemnt) we can finally get what the real attachments are

Does the URL have to be the actual pdf or a link to a comment, scraping the pdf?
- No just take attachment URL's
'''

import requests
from dotenv import load_dotenv
load_dotenv()

# ATTACHMENT_URL = os.getenv('ATTACHMENT_URL')
# SERVER_URL = "http://127.0.0.1:5000/"

"""
Client receives url to the attachment and url to the server

TODO: Client sends data, not attachment
TODO: Client does not save to disk, but saves the data? hmm
"""
class Client():

    def __init__(self, attachment_url, server_url):
        self.attachment_url = attachment_url
        self.server_url = server_url
        attach_requests = requests.get(self.attachment_url)
        # Needs to check if this works for other files, future testing note
        self.file_name = attach_requests.headers['Content-Disposition'].split('"')[1]
        self.content = attach_requests.content

    # This function saves the pdf to disk from the url
    def save_to_disk(self):
        with open(self.file_name, 'wb') as f:
            f.write(self.content)

    # This function send the attachment url to the server
    def send_data(self):
        # Have to make sure encodings are always bytes represented, future testing note
        requests.post(self.server_url + "/attachment", data=self.content)

# Run these two lines to test it out
client_test = Client('https://downloads.regulations.gov/EPA-HQ-OW-2021-0602-0130/attachment_1.pdf', "http://127.0.0.1:5000")
client_test.send_data()

#TODO: Make an argsparse that allows the user input url of attachments below