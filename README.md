## How to Run with Docker
1. Clone the repo to your machine.
2. Change to the root directory of the repo `cd bitly`
3. Build the docker image `docker build -t bitly .`
4. Run the unit tests `docker run bitly python -m pytest`
	* You should see a report printed to the command line showing all tests have passed
5. Run the program `docker run bitly python app.py`
	* You should see the results of the program printed to the command line

## How to Run with Pip
1. Clone the repo to your machine.
2. Change to the root directory of the repo `cd bitly`
3. Create a virtual environment `python -m venv env`
4. Activate the virtual environment `. env/bin/activate` 
5. Install the dependencies `pip install -r requirements.txt`
6. Run the unit tests `python -m pytests`
	* You should see a report printed to the command line showing all tests have passed
7. Run the program `python app.py`
	* You should see the results of the program printed to the command line

## Dependencies
python 3.10.10 (other versions not tested but should work)
pandas 2.0.1
pytest 7.3.1

