"""
 Created by ldh on 19-11-20
"""
from app import create_app

__author__ = "ldh"

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899, debug=app.config['DEBUG'])
