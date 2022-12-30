from fastapi import APIRouter, HTTPException
from services.pokedex_service import PokedexService
import logging

router = APIRouter(
    prefix="/pokedex",
    tags=["pokedex"],
)

logger = logging.getLogger(__name__)

@router.get("/name/{name}")
async def get_pokemon_by_name(name: str) -> dict:
    try:
        logger.info(f"Get pokemon {name} info")
        return PokedexService.get_pokemon_by_name(name=name)
    except Exception:
        raise


@router.get("/id/{id}")
async def get_pokemon_by_id(id: int) -> dict:
    try:
        logger.info(f"Get pokemon id-{id} info")
        return PokedexService.get_pokemon_by_id(id=id)
    except Exception:
        raise
