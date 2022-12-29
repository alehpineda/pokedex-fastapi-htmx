import requests
from dao.pokedex_dao import PokedexDao
from fastapi import HTTPException


class PokedexService:
    @classmethod
    def get_pokemon_by_name(cls, name: str) -> dict:
        try:
            result = PokedexDao.select_pokemon_by_name(name=name)
            if result.get("name", None):
                return result
            pokemon = cls._pokemon_api_by_name(name=name)
            return PokedexDao.save_pokemon(pokemon=pokemon)

        except Exception:
            raise

    @classmethod
    def get_pokemon_by_id(cls, id: int) -> dict:
        try:
            result = PokedexDao.select_pokemon_by_id(id=id)
            if result.get("id", None):
                return result
            pokemon = cls._pokemon_by_id(id=id)
            return PokedexDao.save_pokemon(pokemon=pokemon)

        except Exception:
            raise

    @staticmethod
    def _pokemon_api_by_name(name: str) -> dict:
        """
        Makes a GET request to the PokeAPI using the provided name to retrieve information about a Pokemon.

        Parameters:
        - name (str): The name of the Pokemon to retrieve information for.

        Returns:
        - Response: A requests Response object containing the response from the PokeAPI.
        """
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            response = requests.get(
                url=url,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()  # response.json is a python dict
        except requests.exceptions.HTTPError as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except requests.exceptions.SSLError as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except requests.exceptions.Timeout as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except requests.exceptions.RequestException as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except Exception as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")

    @staticmethod
    def _pokemon_by_id(id: int) -> dict:
        """
        Makes a GET request to the PokeAPI using the provided ID to retrieve information about a Pokemon.

        Parameters:
        - id (int): The ID of the Pokemon to retrieve information for.

        Returns:
        - Response: A requests Response object containing the response from the PokeAPI.
        """
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{id}"
            response = requests.get(
                url=url,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except requests.exceptions.SSLError as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except requests.exceptions.Timeout as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except requests.exceptions.RequestException as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
        except Exception as err:
            raise HTTPException(status_code=response.status_code, detail=f"{err}")
