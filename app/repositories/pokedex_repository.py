import json
from typing import List

from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from entities.pokedex import Pokedex


class PokedexRepository:
    @classmethod
    def select_pokemon_by_name(cls, engine: Engine, name: str) -> List[Pokedex]:
        try:
            with Session(bind=engine) as session:
                statement = select(Pokedex).where(Pokedex.name == name)
                results = session.exec(statement=statement)
                return [result for result in results if result]

        except Exception:
            raise

    @classmethod
    def select_pokemon_by_id(cls, engine: Engine, id: int) -> List[Pokedex]:
        try:
            with Session(bind=engine) as session:
                statement = select(Pokedex).where(Pokedex.id == id)
                results = session.exec(statement=statement)
                return [result for result in results if result]

        except Exception:
            raise

    @classmethod
    def save_pokemon_to_pokedex(cls, engine: Engine, pokemon: dict) -> Pokedex:
        try:
            new_pokemon = Pokedex(
                id=pokemon.get("id"),
                name=pokemon.get("name"),
                api_response=json.dumps(pokemon, indent=4),
            )
            with Session(bind=engine) as session:
                session.add(new_pokemon)
                session.commit()
                session.refresh(new_pokemon)
                return new_pokemon

        except IntegrityError:
            raise
        except Exception:
            raise
