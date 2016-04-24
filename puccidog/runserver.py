"""
This script runs the puccidog application using a development server.
"""

from os import environ
from puccidog import app, lm

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    if HOST == 'localhost':
        app.debug = True
    app.run(HOST, PORT)
