import logging

from flask import request
from flask_restplus import Resource

from jazz.api import api

log = logging.getLogger(__name__)
ns = api.namespace('healthcheck', description='Communication test.')


@ns.route('/')
class HealhCheck(Resource):
    @ns.response(code=400, description='Bad Request')
    def get(self):
        """
        Healhcheck endpoint.
        """
        logging.info('Healthcheck: The request was fulfilled.')
        
        return {
            'message': 'The request was fulfilled.',
            "status_code": 200
            }
