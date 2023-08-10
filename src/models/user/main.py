from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UsersSchema( BaseModel ):

    name_user                   : str               = Field(...)
    gender_user                 : str               = Field(...)
    state_user                  : str               = Field(...)
    municipality_user           : str               = Field(...)


    class Config:
        schema_extra = {
            "example" : {
                "name_user"                 : "Saul Mauricio",
                "gender_user"               : "Hombre",
                "state_user"                : "México",
                "municipality_user"         : 'Chimalhuacán'
            }
        }

class UpdateUserModel(BaseModel):

    name_user                   : Optional[str]
    gender_user                 : Optional[str]
    state_user                  : Optional[str]
    municipality_user           : Optional[str]

    class Config:
        schema_extra = {
            "example" : {
                "name_user"                 : "Saul Mauricio",
                "gender_user"               : "Hombre",
                "state_user"                : "México",
                "municipality_user"         : 'Chimalhuacán'
            }
        }