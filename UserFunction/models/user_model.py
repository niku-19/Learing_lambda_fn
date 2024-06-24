"""
The `User` class is a Pydantic model that represents a user in the application. It defines the fields and validation rules for a user's data, including:

- `firstName`: The user's first name, a non-empty string between 2 and 15 characters long.
- `lastName`: The user's last name, a non-empty string between 2 and 15 characters long.
- `age`: The user's age, an integer between 0 and 120.
- `email`: The user's email address, a valid email string.
- `phoneNumber`: The user's phone number, a string that matches the pattern `^\+?1?\d{9,15}`.
- `password`: The user's password, a non-empty string with at least 8 characters, at least one digit, one uppercase letter, one lowercase letter, and one special character.
- `isEnabled`: A boolean indicating whether the user is enabled or not.
- `birthday`: The user's birthday, a string or a `datetime.datetime` object.
- `createdAt`: The timestamp when the user was created, a string.
- `updatedAt`: The timestamp when the user was last updated, a string.

The class also includes several validation methods to ensure the data integrity of the user's information.
"""


import datetime
import re
from pydantic import BaseModel, EmailStr, Field, StrictBool, StrictInt, StrictStr, field_validator, model_validator, validator
import os
from bson import ObjectId
import bcrypt

DATE_TIME_FORMAT = os.environ.get('DATE_TIME_FORMAT','%Y-%m-%d %H:%M:%S')


class User(BaseModel):
    # id : StrictStr = Field(default_factory = lambda: str(ObjectId()), alias="_id") 
    firstName: StrictStr = Field(..., min_length=2, max_length=15)
    lastName: StrictStr = Field(..., min_length=2, max_length=15)
    age: StrictInt = Field(..., ge=0, le=120)
    email: EmailStr
    phoneNumber: StrictStr = Field(..., pattern=r'^\+?1?\d{9,15}$')
    password: StrictStr = Field(..., min_length=8)
    isEnabled: StrictBool
    birthday: StrictStr  | datetime.datetime  # FIXME: SHOULD ONLY ACCEPT DATE-TIME FORMATE STRING
    createdAt: str = Field(default_factory = lambda: datetime.datetime.strptime(str(datetime.datetime.now().strftime(DATE_TIME_FORMAT)) , DATE_TIME_FORMAT))
    updatedAt: str = Field(default_factory = lambda: datetime.datetime.strptime(str(datetime.datetime.now().strftime(DATE_TIME_FORMAT)) , DATE_TIME_FORMAT))

    @model_validator(mode='before')
    @classmethod
    def check_required_fields(cls, values):
        required_fields = ['firstName', 'lastName', 'age', 'email', 'phoneNumber', 'password', 'isEnabled']
        missing_fields = [field for field in required_fields if field not in values]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        return values

    @field_validator('password')
    def validate_password(cls, value):
        if not re.search(r'\d', value):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', value):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\W', value):
            raise ValueError('Password must contain at least one special character')

        hashed_password = bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        return hashed_password
    
    @field_validator('phoneNumber')
    def validate_phoneNumber(cls, value):
        if not re.search(r'^\+?1?\d{9,15}$', value):
            raise ValueError('Invalid phone number')
        return value 

    @field_validator('birthday')
    def validate_birthday_date(cls, value):
        try:
            parsed_date = datetime.datetime.strptime(value, DATE_TIME_FORMAT)
            return parsed_date
        except ValueError:
            raise ValueError(f"createdAt must be in the format {DATE_TIME_FORMAT}")       

    @field_validator('createdAt')
    def validate_created_at(cls , value):
        try:
            parsed_date = datetime.datetime.strptime(value, DATE_TIME_FORMAT)
            return parsed_date
        except ValueError:
            raise ValueError(f"createdAt must be in the format {DATE_TIME_FORMAT}")
        
    @field_validator('updatedAt')
    def validate_updated_at(cls , value):
        try:
            parsed_date = datetime.datetime.strptime(value, DATE_TIME_FORMAT)
            return parsed_date
        except ValueError:
            raise ValueError(f"createdAt must be in the format {DATE_TIME_FORMAT}")
        




