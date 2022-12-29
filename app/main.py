import uvicorn
from controllers import pokedex_controller
from fastapi import FastAPI

app = FastAPI()

app.include_router(pokedex_controller.router)


@app.get("/")
async def root():
    return {"message": "Pokedex App Online!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
