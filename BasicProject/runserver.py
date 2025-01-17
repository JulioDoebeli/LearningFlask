"""
This script runs the BasicProject application using a development server.
"""

from os import environ
from BasicProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555 
        """COMENT"""
    app.run(HOST, PORT)
