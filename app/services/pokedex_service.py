import requests
import json
from requests import Response


def get_pokemon_by_name(name: str) -> Response:
    try:
        # call db
        # if exists return json as dict
        # else call api and save pokemon entry
        response = _pokemon_api_by_name(name=name)
        # response.json() is a python dict
        # json.dumps(dict, indentation)
        pokemon = response.json()
        return response
    except Exception:
        raise


def get_pokemon_by_id(id: int) -> Response:
    try:
        return _pokemon_by_id(id=id)
    except Exception:
        raise


def _pokemon_api_by_name(name: str) -> Response:
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
        return response
    except requests.exceptions.SSLError as exp:
        return {"SSLError": exp}
    except requests.exceptions.Timeout as exp:
        return {"Timeout Exception": exp}
    except requests.exceptions.RequestException as exp:
        return {"Request Exception": exp}
    except Exception as exp:
        return {"General Exception": exp}


def _pokemon_by_id(id: int) -> Response:
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
        return response
    except requests.exceptions.SSLError as exp:
        return {"SSLError": exp}
    except requests.exceptions.Timeout as exp:
        return {"Timeout Exception": exp}
    except requests.exceptions.RequestException as exp:
        return {"Request Exception": exp}
    except Exception as exp:
        return {"General Exception": exp}
