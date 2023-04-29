import mysql.connector
from django.conf import settings


def connect():
    config = {
        'user': settings.DATABASES['default']['USER'],
        'password': settings.DATABASES['default']['PASSWORD'],
        'host': settings.DATABASES['default']['HOST'],
        'database': settings.DATABASES['default']['NAME'],
        'port': settings.DATABASES['default']['PORT'],
        'raise_on_warnings': True
    }
    cnx = mysql.connector.connect(**config)
    return cnx


def disconnect(cnx):
    cnx.close()