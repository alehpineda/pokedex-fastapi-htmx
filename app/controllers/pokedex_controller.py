import requests
from fastapi import APIRouter, HTTPException

from services.pokedex_service import PokedexService

router = APIRouter(
    prefix="/pokedex",
    tags=["pokedex"],
)


@router.get("/name/{name}")
async def get_pokemon_by_name(name: str) -> dict:
    try:
        return PokedexService.get_pokemon_by_name(name=name)
    except Exception:
        raise


@router.get("/id/{id}")
async def get_pokemon_by_id(id: int) -> dict:
    try:
        return PokedexService.get_pokemon_by_id(id=id)
    except Exception:
        raise
