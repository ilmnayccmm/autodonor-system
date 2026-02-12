import psycopg2

try:
    conn = psycopg2.connect(
        dbname="telegram_bot_db",
        user="postgres",
        password="ss2121zz",
        host="localhost",
        port="5432"
    )
    print("Connected!")
except psycopg2.OperationalError as e:
    print("Error:", e)
finally:
    try:
        conn.close()
    except NameError:
        pass
