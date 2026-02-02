import sqlite3

DB_NAME = "ias.db"


def connect_db():
    """Підключення до бази даних і вивід версії SQLite"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version();")
        version = cursor.fetchone()
        print(f"[OK] Підключено до SQLite, версія: {version[0]}")
        return conn
    except sqlite3.Error as e:
        print(f"[ERROR] Помилка підключення: {e}")
        return None


def search_resources(keyword):
    """
    Пошук ресурсу за типом або локацією
    (текстовий пошук)
    """
    conn = connect_db()
    if not conn:
        return []

    cursor = conn.cursor()
    query = """
    SELECT resource_id, type, location, status
    FROM resources
    WHERE type LIKE ? OR location LIKE ?
    """
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    conn.close()

    return results


def check_alarm(value, threshold=60):
    """
    Логічний фільтр 'Тривога'
    value — числовий показник
    threshold — граничне значення
    """
    if value > threshold:
        return "WARNING"
    else:
        return "OK"


if __name__ == "__main__":
    # 7. Перевірка підключення
    conn = connect_db()
    if conn:
        conn.close()

    print("\n--- Пошук ресурсів ---")
    results = search_resources("Екіпаж")
    for row in results:
        print(row)

    print("\n--- Перевірка тривоги ---")
    test_values = [30, 75, 50, 90]
    for v in test_values:
        status = check_alarm(v)
        print(f"Значення: {v} → Статус: {status}")
