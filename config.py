from os import environ

#Env variables
TEMPLATE_DATABASE_URI=environ.get('DATABASE_URI', 'sqlite://')