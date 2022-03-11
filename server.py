
from flask import Flask, request
import pdfplumber

app = Flask(__name__)

"""
Server receives post request from Client with URL content.
"""
@app.route('/attachment', methods=['POST'])
def saves_content():
    data = request.get_data()
    save_to_disk(data)
    extract_pdf_to_txt('attachment.pdf')
    return "Received"

"""
Writes attachment content and extracted text from PDF to disk
URL's can be found in README
"""
def save_to_disk(data):
    with open("attachment.pdf", 'wb') as f:
        f.write(data)
    
'''
Extracts text from PDF
'''
def extract_pdf_to_txt(pdf):
    with pdfplumber.open('attachment.pdf') as pdf:
        file = pdf.pages
        with open('attachment.txt', 'w') as f:
            for page in file:
                f.write(page.extract_text())


if __name__ == "__main__":
    app.run()