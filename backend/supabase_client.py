from supabase import create_client
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener URL y clave de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Falta SUPABASE_URL o SUPABASE_KEY en el entorno.")

# Crear cliente de Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def guardar_instruccion(texto: str, respuesta: str):
    """
    Guarda una instrucción y su respuesta en la tabla 'instructions' de Supabase.

    Args:
        texto (str): La instrucción enviada por el usuario.
        respuesta (str): La respuesta generada por OpenAI.

    Returns:
        dict: Respuesta de Supabase si la operación es exitosa.
        None: Si ocurre un error durante la operación.
    """
    try:
        # Insertar los datos en la tabla "instructions"
        response = supabase.table("instructions").insert({
            "text": texto,
            "respuesta": respuesta
        }).execute()

        # Verificar si la respuesta es exitosa
        if response.data:
            print("✅ Instrucción y respuesta guardadas correctamente.")
            return response.data
        else:
            print(f"❌ Error al guardar: {response.error_message}")
            return None

    except Exception as e:
        # Manejo de errores
        print(f"❌ Error al guardar en Supabase: {e}")
        return None
