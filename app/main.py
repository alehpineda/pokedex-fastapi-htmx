from fastapi import FastAPI

from controllers import pokedex_controller

app = FastAPI()

app.include_router(pokedex_controller.router)


@app.get("/")
async def root():
    return {"message": "Pokedex App Online!"}
