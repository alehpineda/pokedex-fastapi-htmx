from sqlmodel import Field, SQLModel


class Pokedex(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    api_response: str
