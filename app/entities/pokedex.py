from sqlmodel import Field, SQLModel


class Pokedex(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    api_response: str
