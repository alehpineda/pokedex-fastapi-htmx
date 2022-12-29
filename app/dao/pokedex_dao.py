import json

from config.db_config import DatabaseConfig
from entities.pokedex import Pokedex
from repositories.pokedex_repository import PokedexRepository


class PokedexDao:

    db_filename = "db/pokedex.db"
    db_config = DatabaseConfig(db_filename)
    engine = db_config.engine()

    @classmethod
    def select_pokemon_by_name(cls, name: str) -> dict:
        results = PokedexRepository.select_pokemon_by_name(engine=cls.engine, name=name)
        if results:
            return json.loads(results[0].api_response)
        return {}

    @classmethod
    def select_pokemon_by_id(cls, id: int) -> dict:
        results = PokedexRepository.select_pokemon_by_id(engine=cls.engine, id=id)
        if results:
            return json.loads(results[0].api_response)
        return {}

    @classmethod
    def save_pokemon(cls, pokemon: dict) -> dict:
        try:
            new_pokemon = PokedexRepository.save_pokemon_to_pokedex(
                engine=cls.engine, pokemon=pokemon
            )
            return json.loads(new_pokemon.api_response)
        except Exception:
            raise
