import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from http_client_api import CMCHTTPClient
from config import settings

app = FastAPI()
cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://192.168.0.191/:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/cryptocurrencies')
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@app.get('/cryptocurrency/{currency_id}')
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id=currency_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7777, reload=True)