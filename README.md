# Shorten URL

This application takes in an URL and shortens it. On following the shortened URL you will be
redirected to the original webpage.

Note that each url gets mapped to a single shortened url, this is done to minimize collisions.
The last "/" is not stripped from the url, and hence https://google.com and https://google.com/
will map to different shortened urls.

## Testing

The application has been tested manually. In the interest of time, the unit tests have not been
included as a part of this app. However, that is something high on the priority list.

## Environment

- Language: `Python-3.11.0.`
- Database: `SQLite`
- ORM: `SQLAlchemy`
- Serializer/Deserializer: `Marshmallow` - This has been set up, however it is not being used.

## Docker build

Please ensure docker is installed and running. Also ensure that the docker-compose binary
is in the path.
To set up the app using docker. From within the project directory, please run:

`docker-compose up`

:warning: **VPNs tend to interfere with docker networking and when downloading packages**
It is recommended to turn the VPN off until the build completes.

#### Access the app.

The containerized application should be available at:

http://127.0.0.1/

## Running locally

It is suggested you create a virtual environment if you wish to run the application locally.
To do this please follow the given steps

`python3 -m venv venv`

#### Activate the virtual environment

`source venv/bin/activate`

#### Install the required pacakages

`pip3 install -r requirements.txt`

#### Insure the database file is all setup.

This will ideally be handled using migration, however for a single object model this script works
well.

`python bin/db_setup.py`

#### Start the app.

`python3 main.py`

#### Access the app.

The application should now be available at:

http://127.0.0.1:8888/

