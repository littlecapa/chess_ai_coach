import pyodbc

# Replace these with your actual credentials
server = 'cacsqlserver.database.windows.net'
database = 'cac_db'
username = 'cac_db_admin@cacsqlserver'
password = 'LC_G7q!mP4zR@t2'

# Connection string
conn_str = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_str, timeout=5)
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:")
    print(e)