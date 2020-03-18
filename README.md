# pytest_fixure_example

Small example of using pytest with fixtures for the database.

Based on https://medium.com/@mariusz.raczynski2/pytest-mock-how-to-mock-your-database-connection-5c84a5a0bfc3


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Clone the project from github, e.g.:

    git clone https://github.com/jessamynsmith/pytest_fixure_example.git
    
Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv pytest_fixure_example --python=/path/to/python3
    pip install -r requirements.txt

Run tests:

    python -m pytest
