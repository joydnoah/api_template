from os import environ

#Env variables
TEMPLATE_DATABASE_URI=environ.get('TEMPLATE_DATABASE_URI', 'sqlite://')