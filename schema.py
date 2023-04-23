from marshmallow import Schema, fields


class URLMappingSchema(Schema):
    id = fields.UUID()
    long_url = fields.Url()
    short_url_id = fields.String()
