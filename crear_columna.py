# -*- coding: utf-8 -*-
import subprocess
import sys

print("Creando columna 'Precio Compra Usados'...")

try:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "supabase"], check=False)
    from supabase import create_client

    supabase = create_client("https://umftwvbvzqnkuiqkdmya.supabase.co",
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVtZnR3dmJ2enFua3VpcWtkbXlhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4OTA0Nzc5MCwiZXhwIjoyMTA0NjIzNzkwfQ.GhQRhP93yBTZt-9v_Q1v0oPsvzjSEZQV2I8OEA3xIQg")

    # Insertar test con la nueva columna
    test = {"Patente": "TEMP123", "Marca": "T", "Modelo": "T", "VIN": "T",
            "Responsable": "T", "Sucursal": "T", "Precio Compra Usados": "1000"}
    supabase.table('vehiculos').insert([test]).execute()
    supabase.table('vehiculos').delete().eq('Patente', 'TEMP123').execute()

    print("[OK] Columna creada exitosamente!")

except Exception as e:
    print("[ERROR] {}".format(str(e)))
    print("\nHazlo manualmente en Supabase:")
    print("1. https://supabase.com -> umftwvbvzqnkuiqkdmya")
    print("2. SQL Editor")
    print('3. ALTER TABLE vehiculos ADD COLUMN IF NOT EXISTS "Precio Compra Usados" TEXT DEFAULT NULL;')
    print("4. Ctrl+Enter")
