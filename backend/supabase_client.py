from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def guardar_instruccion(texto: str):
    try:
        response = supabase.table("instructions").insert({"text": texto}).execute()
        print("✅ Instrucción guardada.")
        return response
    except Exception as e:
        print("❌ Error al guardar instrucción:", e)
        return None