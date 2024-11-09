from fastapi import FastAPI
from api.routers.query_mind import router 

def init_routers(app: FastAPI) -> None:
    app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI(
        title='QueryMind API',
        description='QuerMind, Mİlvus vektör veritabanını kullanarak datada bulunan blog metinini embedding haline getiren ve bu verilere dayalı sorulara yapay zaka destekli yanıtlar üreten bir sistemdir.',
        version='1.0.0',
    )
    init_routers(app)
    return app

app = create_app()