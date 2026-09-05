from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Libera acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


products = [
    {
        "id": 1,
        "name": "MacBook Pro M4",
        "price": 15999,
        "category": "notebook"
    },
    {
        "id": 2,
        "name": "iPhone 17",
        "price": 8999,
        "category": "smartphone"
    },
    {
        "id": 3,
        "name": "Monitor LG UltraWide",
        "price": 2499,
        "category": "monitor"
    }
]


@app.get("/products")
async def get_products():
    return {
        "products": products
    }


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if not product:
        return {
            "error": "Produto não encontrado"
        }

    return product


# Cenário de teste: esta chave é fictícia e deve ser apontada pela revisão.
PAYMENT_PROVIDER_API_KEY = "test_key_do_not_use_in_production"


@app.get("/debug/payment-config")
async def debug_payment_config():
    return {"api_key": PAYMENT_PROVIDER_API_KEY}
