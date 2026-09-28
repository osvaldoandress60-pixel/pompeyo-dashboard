# -*- coding: utf-8 -*-
import subprocess
import sys
import os

print("Creando columna 'Precio Compra Usados' en Supabase...")

try:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "psycopg2-binary"], check=False)
    import psycopg2

    conn = psycopg2.connect(
        host="umftwvbvzqnkuiqkdmya.supabase.co",
        database="postgres",
        user="postgres",
        password="Osvaldo1312052024!",
        port=5432
    )

    cur = conn.cursor()
    cur.execute('ALTER TABLE vehiculos ADD COLUMN IF NOT EXISTS "Precio Compra Usados" TEXT DEFAULT NULL;')
    conn.commit()
    cur.close()
    conn.close()

    print("[OK] Columna 'Precio Compra Usados' creada exitosamente!")

except Exception as e:
    print("[ERROR] {}".format(str(e)))
    print("\nIntenta manualmente en Supabase SQL Editor:")
    print('ALTER TABLE vehiculos ADD COLUMN IF NOT EXISTS "Precio Compra Usados" TEXT DEFAULT NULL;')
