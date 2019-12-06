# Flask API template
Base flask configuration for an API proyect that connects to a postgresql database.

## Run service
To run the service follow the following lines.

First install the requirements using:
```
pip install -r requirements.txt
```

After installing the required libs run the service using the line:
```
python manage.py runserver
```

By default the service tuns on localhost:5000 to change the port you can add the line __-p PORT__ to choose a different one
```
python manage.py runserver -p PORT
```

## Enviroment variables
The config.py file contains the enviroment variables to run the project:

* TEMPLATE_DATABASE_URI = Uri of the database to connect with. Ie. _postgres://username:password@localhost:5432/localDB_