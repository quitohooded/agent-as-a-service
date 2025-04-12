from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI, APIError
from dotenv import load_dotenv
import os
from supabase_client import guardar_instruccion

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("La API Key de OpenAI no está configurada.")

# Inicializar cliente OpenAI
client = OpenAI(api_key=api_key)

# Inicializar app FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar a dominios específicos en producción
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

# Ruta principal
@app.post("/instruccion")
async def enviar_instruccion(req: InstruccionRequest):
    instruccion = req.instruccion.strip()

    if not instruccion:
        return {"error": "La instrucción está vacía."}

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": instruccion}]
        )
        respuesta_texto = response.choices[0].message.content
    except APIError as e:
        raise HTTPException(status_code=500, detail=f"Error al comunicarse con OpenAI: {str(e)}")

    try:
        if guardar_instruccion(instruccion, respuesta_texto) is None:
            return {"respuesta": respuesta_texto, "error": "No se pudo guardar en Supabase"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar en Supabase: {str(e)}")

    return {"respuesta": respuesta_texto}