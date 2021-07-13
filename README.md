# python-api-demo

## Requirements

* UNIX based command-line.
* Admin rights in your machine
* GIT installed in your machine.
* Python 3 installed in your machine.
* Postman or equivalent tool. 
  * https://www.postman.com/downloads/
  * Please find my API calls here. https://www.getpostman.com/collections/640fed8fadedd245e89e
* Please note that for the MS Windows environment this README.md instructions are different. 

## Instructions
* Please clone the repository in your machine.
  * ``git clone https://github.com/AratioD/python-api-demo.git``

* Please install Python virtual environment.
    * `python3 -m pip install virtualenv`
  
* Please create a virtual environment.
  * `virtualenv venv --python=python3.8`
  
* Launch a virtual environment from UNIX command-line.
  *  `source venv/bin/activate`
  
* Please install all requirements in the virtual environment.
  *  `pip install -r requirements.txt`
  
* Launch the application from command-line.
  * ``python app.py``
  
* Use API calls through Postman.

* Use API calls through browser.
  * http://127.0.0.1:80/amounts
  * http://127.0.0.1:80/names
  * http://127.0.0.1:80/amount
  * http://127.0.0.1:80/name/timo

* Close virtual environment
  * `deactivate`

## Instructions Docker-Compose

* Please install Python virtual environment.
  * `docker-compose up`
