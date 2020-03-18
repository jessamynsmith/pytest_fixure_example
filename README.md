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

Check code style:

    flake8

(Optional) Generate graph of data models. In order to do this, you will need to install some extra requirements:

    brew install graphviz pkg-config
    pip install -r requirements/extensions.txt
    
You can then generate graphs, e.g.:

    python manage.py graph_models --pygraphviz -a -g -o all_models.png  # all models
    python manage.py graph_models periods --pygraphviz -g -o period_models.png  # period models

Run server:

    python manage.py runserver
    
Or run using gunicorn:

    gunicorn eggtimer.wsgi

Lint JavaScript:

    ./node_modules/jshint/bin/jshint */static/*/js

Run JavaScript tests:

    mocha --require-blanket -R html-cov */tests/static/*/js/* > ~/eggtimer_javascript_coverage.html

To run Selenium tests, you must have chromedriver installed:

     brew install chromedriver

Next you need to create a Django admin user and then export the email and password for that user as environment variables:

    export SELENIUM_ADMIN_EMAIL='<EMAIL_VALUE>'
    export SELENIUM_ADMIN_PASSWORD='<PASSWORD_VALUE>'

Finally, ensure the server is running, and run the selenium tests:

    nosetests selenium/

Retrieve data from the API with curl. <AUTH_TOKEN> can be found in your account info.

curl -vk -X GET -H "Content-Type: application/json" -H 'Authorization: Token <AUTH_TOKEN>' "https://eggtimer.herokuapp.com/api/v2/statistics/" | python -m json.tool

curl -vk -X GET -H "Content-Type: application/json" -H 'Authorization: Token <AUTH_TOKEN>' "https://eggtimer.herokuapp.com/api/v2/periods/" | python -m json.tool

You can filter based on minimum and maximum timestamp of the events:

curl -vk -X GET -H "Content-Type: application/json" -H 'Authorization: Token <AUTH_TOKEN>' "https://eggtimer.herokuapp.com/api/v2/periods/?min_timestamp=2016-01-19&max_timestamp=2016-01-20" | python -m json.tool

Create a period:

curl -vk -X POST -H "Content-Type: application/json" -H 'Authorization: Token <AUTH_TOKEN>' --data '{"timestamp": "<YYYY-MM-DD>T<HH:MM:SS>"}' "https://eggtimer.herokuapp.com/api/v2/periods/" 

### Continuous Integration and Deployment

This project is already set up for continuous integration and deployment using circleci, coveralls,
and Heroku.

Make a new Heroku app, and add the following addons:

    Heroku Postgres
	SendGrid
	New Relic APM
	Papertrail
	Heroku Scheduler
	Dead Man's Snitch

Add Heroku buildpacks:

    heroku buildpacks:set heroku/nodejs -i 1
    heroku buildpacks:set heroku/python -i 2

Enable the project on coveralls.io, and copy the repo token

Enable the project on circleci.io, and under Project Settings -> Environment variables, add:

    COVERALLS_REPO_TOKEN <value_copied_from_coveralls>
    HEROKU_API_KEY <value_copied_from_heroku>

On circleci.io, under Project Settings -> Heroku Deployment, follow the steps to enable
Heroku builds. At this point, you may need to cancel any currently running builds, then run
a new build.

Once your app is deployed successfully, you can add the Scheduler task on Heroku:

    python manage.py notify_upcoming_period --settings=eggtimer.settings

You can also set up Dead Man's Snitch so you will know if the scheduled task fails.


Thank you to:
Emily Strickland (github.com/emilyst) for the name

