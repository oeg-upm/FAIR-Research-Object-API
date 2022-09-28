# ROCrate_enrichment_service
## AUTHOR: George Hadib

# Introduction:
FAIROs is a service to assess the FAIRness of Research Objects. The service offers a RESTFUL API built with the FLASK library for python. It receives a ZIP file with the ro-crate Research Object and return the assessment. Signing up to the service is a manual process managed locally by the service provider. Passwords are encrypted using the sha256 algorithm. However, the rest of the operations are available through the public API.

# The API:
The project has a restful API designed with flask on python. A description of the file can be found [here](https://app.swaggerhub.com/apis/esgg/FAIROs/1.0.0-oas3)

# How to use?
## Deployment:
To run the server make sure to have python3.10 and pip installed in your machine and then follow the following steps:
Step 1 : Clone the repository

`git clone https://github.com/oeg-upm/FAIR-Research-Object-API.git`

Step 2 : Go inside the folder

`cd FAIR-Research-Object-API`

Step 3 : Install requirements

`pip install -r requirements.txt`

Step 4 : Create a new user
. In order to do so, open the script called client.py with a text editor, edit the dictionary called entry_json in line #30 with your username and password and finally run the script. 

Step 5 : Change the SECRET_KEY used to encrypt the passwords to a key of your choice. 
. To do so, open the script called API_Server.py with a text editor and enter the new key in the variable SECRET_KEY in line #10

Step 5 : Run the application

`py run.py`, `py3 run.py`, `python run.py` or `python3 run.py`. This depends on your local environment.



A successful use case of this service is divided in three phases:

## Phase I:
The user sends a json/jsonld file using a POST method to the URI:
`http://domainname.upm.es/api/jobs/`

After receiving the payload, the server responds with status_code of 201 and a ticket in a json payload. This ticket should be collected by the client for it's further use during Phase II.


## Phase II:
The user sends a GET request with the ticket collected from Phase I, the server checks the status of the request involved and responds due to the found results. If the ticket is invalid, the server responds with a 400 status code. If the request is yet to be attended, the server responds with a 200 status code and a "Please try again later" message.

## Phase III:
The user sends a GET request woth the tocket and the token to the server. The server basically reapeats the validations of the GET jobs and if everything is fine, it sends the file to the user.

