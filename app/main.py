import logging
from utils.custom_logging import CustomizeLogger
from controllers import pokedex_controller
from fastapi import FastAPI
from pathlib import Path


logger = logging.getLogger(__name__)

config_path=Path("utils/logging_config.json")

app = FastAPI(
    title="Pokedex|Fastapi|HTMX",
    debug=True
)

logger = CustomizeLogger.make_logger(config_path)

app.logger = logger

app.include_router(pokedex_controller.router)


@app.get("/health")
async def root():
    logger.info("Pokedex App Online!")
    return {"message": "Pokedex App Online!"}
