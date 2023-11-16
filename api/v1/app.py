#!usr/bin/python3
"""falsk app"""
from api.v1.views import app_views
from flask import Flask
from os import environ


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    """ Main Function """
    host = environ.get('KNS_API_HOST')
    port = environ.get('KNS_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
