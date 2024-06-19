import uvicorn
from fastapi import FastAPI

from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router
# from shared.database import engine, Base

# from contas_a_pagar_e_receber.models.conta_a_pagar_receber_model import ContaPagarReceber
#
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def i_am_programmer() -> str:
    return "Hi, I am a Programmer!"


app.include_router(contas_a_pagar_e_receber_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
