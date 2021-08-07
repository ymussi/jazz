from marshmallow import Schema, fields, validate

class BazookaSchema(Schema):
    text = fields.String(description='Bazooka message', required=True)
