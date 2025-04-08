from fastapi import FastAPI, Request
import httpx

app = FastAPI()

# Pegá acá la URL del webhook de prueba de n8n (Test URL)
N8N_TEST_WEBHOOK = "http://localhost:5678/webhook-test/test"

@app.post("/instruccion")
async def enviar_instruccion(request: Request):
    data = await request.json()
    instruccion = data.get("instruccion")

    async with httpx.AsyncClient() as client:
        response = await client.post(N8N_TEST_WEBHOOK, json={"mensaje": instruccion})

    return {
        "status": response.status_code,
        "respuesta": response.json()
    }
