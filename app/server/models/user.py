from typing import Optional

from pydantic import BaseModel,EmailStr, Field

class UserSchema(BaseModel):
    userid: int = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "userid": 1,
                "username": "admin",
                "password": "adminpassword",
                "email": "admin@gmail.com"
            }
        }


class UpdateUserModel(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]


    class Config:
        schema_extra = {
             "example": {
                "userid": 1,
                "username": "admin",
                "password": "adminpassword",
                "email": "admin@gmail.com"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
