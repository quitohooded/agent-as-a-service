from supabase_client import supabase

def test_connection():
    try:
        response = supabase.table("test").select("*").execute()
        print("✅ Conexión exitosa. Datos:", response.data)
    except Exception as e:
        print("❌ Error en la conexión:", e)

test_connection()