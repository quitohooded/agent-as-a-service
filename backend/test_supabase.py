import pytest
from supabase_client import supabase

def test_supabase_connection():
    """
    Verifica que la conexión con Supabase sea exitosa y que se pueda acceder a la tabla 'instructions'.
    """
    try:
        response = supabase.table("instructions").select("*").limit(1).execute()

        assert isinstance(response.data, list), "La respuesta no es una lista."
        print("✅ Conexión exitosa con Supabase. Datos:", response.data)
    except Exception as e:
        pytest.fail(f"❌ Error en la conexión con Supabase: {e}")
