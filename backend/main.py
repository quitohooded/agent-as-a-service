from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
from supabase_client import guardar_instruccion

# Cargar variables de entorno desde .env
load_dotenv()

# Inicializar cliente de OpenAI
client = OpenAI()  # Usa la API key desde OPENAI_API_KEY

# Inicializar app FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquema de la solicitud
class InstruccionRequest(BaseModel):
    instruccion: str

# Ruta de prueba
@app.get("/")
async def root():
    return {"message": "El backend está funcionando."}

# Ruta principal que recibe la instrucción y responde
@app.post("/instruccion")
async def enviar_instruccion(req: InstruccionRequest):
    instruccion = req.instruccion

    guardar_instruccion(instruccion)

    # Llamada al modelo de OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": instruccion}]
    )

    respuesta_texto = response.choices[0].message.content
    return {"respuesta": respuesta_texto}
