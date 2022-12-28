from fastapi import APIRouter

from services import pokedex_service

router = APIRouter(
    prefix="/pokedex",
    tags=["pokedex"],
)


@router.get("/name/{name}")
async def get_pokemon_by_name(name: str) -> dict:
    try:
        return pokedex_service.get_pokemon_by_name(name)
    except Exception:
        raise


@router.get("/id/{id}")
async def get_pokemon_by_id(id: int) -> dict:
    try:
        return pokedex_service.get_pokemon_by_id(id)
    except Exception:
        raise