import logging

from flask import request
from flask_accepts import accepts
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest

from jazz.api import api
from jazz.api.bazooka.schema import BazookaSchema
from jazz.api.bazooka.controller import BazookaController

log = logging.getLogger(__name__)
ns = api.namespace('bazooka', description="Send Bazooka's")

@ns.route("/")
class Consumer(Resource):
    @accepts(schema=BazookaSchema, api=api)
    def post(self):
        """
        Send message to bazooka-nutella channel.

        example:

            {
                "text": "\"message\" from @mention to @mention"
            }
        """
        
        json_data = request.json

        return BazookaController.send_message(json_data)
