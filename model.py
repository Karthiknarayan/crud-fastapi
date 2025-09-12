from pydantic import BaseModel

class Team(BaseModel):
    number_of_titles:str
    team:str
