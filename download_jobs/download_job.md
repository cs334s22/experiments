# Download_jobs Documentation


## Summary
This will going through the pyMongo Data_Storage database and see if the specific job has been added to the database. If it hasnt been added, the jobs id, link, and type is added to a CSV file. 
## Description 
This will start at the beginning at 1972-01-01 00:00:00 and make a CSV file. With three keys. 
The SearchIterator file wil be called, and we will loop through to recieve the specific job from Regulations and its API. 
We will check the Database, and add the job to the CSV if it is not in it. 


## Job_Validator.py 
Gets the specific api, and calls the pyMongo dataStorage. We get the beginning time of when to start. Make the CSV file, add three keys to it, and loop through ***Search Iterator***. If that job is not in the dataStorage, print it's ID, and write the ID, URL, and Type to the CSV file. 

## Search Iterator.py 
Iterate over all date older than a specified date. We the API, URL, next_page number, and its Params to determine that we are using the info from and after the modified data, going 250 pages at a time. We iterate through the params and download the job (url, params) as **Result**. If result's pagenumber is equal to the totalPages, and the totalElements is <= 5000, the Iterator is done. If ot the pages are reset, the times converted to the proper layout, and the Iterator continues to add jobs into **Result**