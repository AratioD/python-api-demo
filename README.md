# python-api-demo

Device requirements UNIX based command-line. Please note that for the MS Windows environment this README.md instructions might be different. 

To use API you'll need Postman or equivalent tool. Please find a download link below.
* https://www.postman.com/downloads/
* Please find my Postman API calls. https://www.postman.com/collections/640fed8fadedd245e89e


Please clone your repository in your machine through command-line.
* ``git clone https://github.com/AratioD/python-api-demo.git``

To use application you'll need
* Install Python virtual environment. Please see commands below.
    * `python3 -m pip install virtualenv`
  
  
* Create a virtual environment. Please see the command below.
  * `virtualenv venv --python=python3.8`
  
* Launch a virtual environment from UNIX command-line.
  *  `source venv/bin/activate`
  * in Windows --> ./venv/Scripts/activate.bat`
  
* Install Flask-RESTful
  *  `pip install Flask-RESTful`
  *  `pip install requests`
  
* Launch a virtual environment from Windows command-line.
  *  `./venv/Scripts/activate.bat`
  
* Launch the application from command-line.
  * python app.py`
  
* Close virtual environment
  * `deactivate`
  