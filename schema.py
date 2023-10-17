from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, ValidationError, fields, validate


class Table_schema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=3, max=20))
    email = fields.String(required=True, validate= [validate.Email(), validate.Length(min=5, max=50)])
    age = fields.Integer(required=True, validate= validate.Range(18,100))
    fav_book = fields.String(required=True, validate= validate.NoneOf(["comics", "pingpong"]))
    gender = fields.String(required=True, validate= validate.OneOf(["male", "female"]))
    


table_schema = Table_schema()

user_data = {'username': 'mohit', 'email': 'jon.doe@gmail.com', 'age': 100, 'fav_book': 'chota bheem', 'gender': 'male'}

try:
    validated_data = table_schema.load(user_data)
    print("done")
    
except ValidationError as e:
    print(f'Validation error: {e.messages}')

