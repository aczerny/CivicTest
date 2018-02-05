CivicTest
Prueba para la empresa CivicBrain(Instagis)

Prerequisites

    1. Install Python 3.6.x from https://www.python.org/downloads/ or c
    Check that python3 has been installed by running it at the terminal:
    $ python3
    >>> Python 3.6.4

    2. Install virtualenv via homebrew 
    $ sudo brew install virtualenv

    3. Create your virtual environment named .venv (in te root project)
    $ python3.6 -m venv .venv


Deployment:

    - Activate your virtual environment:
    $ . .venv/bin/activate

    - Create your database named 'address'(assuming postgres is installed)
    $ createdb address

    - Create Role named 'address'
    $ psql address
    $ create role address with login password '357357';
    $ grant all privileges on database address to address;
    $ ctrl + D

    - Create and run migrations for the new database
    $ ./manage.py makemigrations
    $ ./manage.py migrate

    - Create your first user
    $ ./manage.py createsuperuser
    username:
    mail:
    password:
    password (type agayn):

    - Run project
    $ ./manage.py runserver

    - Go to your internet navigator and put the url:
    http://localhost:8000/admin/

Heroku:

    - See this project running on Heroku:
    URL: https://civictest.herokuapp.com

    - Users:
        - username: jtrh
        - password: CivicBrain

        - username: amenadiel
        - password: CivicBrain

    - Admin:
    URL: https://civictest.herokuapp.com/admin/

    - API:
    URL: https://civictest.herokuapp.com/core/api/address/