'''
Allows clients to send pdf contents from a downloadable link

Comments with attachments are not saved, 
with this (c_Attachemnt) we can finally get what the attachment
'''

from typing_extensions import Required
import requests
import argparse

class Client():

    def __init__(self, attachment_url, server_url):
        self.attachment_url = attachment_url
        attach_requests = requests.get(attachment_url.URL, " ")
        self.server_url = server_url
        self.content = attach_requests.content

    # Saves the pdf to disk from contents
    def save_to_disk(self):
        with open(self.file_name, 'wb') as f:
            f.write(self.content)

    # Send the attachment contents to the server in binary
    def send_data(self):
        # Have to make sure encodings are always bytes represented, future testing note
        requests.post(self.server_url + "/attachment", data=self.content)

'''
run python3 client.py <PDF_url> in terminal
PDFs can be found in README.md
'''
if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Input URL to be downloaded.")
    parser.add_argument("URL")
    attachment_url = parser.parse_args()
    client = Client(attachment_url, "http://127.0.0.1:5000")
    client.send_data()